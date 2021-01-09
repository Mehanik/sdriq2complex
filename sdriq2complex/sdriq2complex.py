#!/usr/bin/env python3
# coding: utf-8

import struct
import numpy as np


def load_sdriq(input_filename: str):
    """Read sdrangel's iq file format

    https://github.com/f4exb/sdrangel/blob/aa0cba102a6ce6b89065ed458533910e5f934d2a/sdrbase/dsp/filerecord.h
        struct Header
        {
            quint32 sampleRate;
            quint64 centerFrequency;
            quint64 startTimeStamp;
            quint32 sampleSize;
            quint32 filler;
            quint32 crc32;
        };

    https://github.com/f4exb/sdrangel/tree/master/rescuesdriq

    Sample rate in S/s (4 bytes, 32 bits)
    Center frequency in Hz (8 bytes, 64 bits)
    Start time Unix timestamp epoch in seconds (8 bytes, 64 bits)
    Sample size as 16 or 24 bits (4 bytes, 32 bits)
    filler with all zeroes (4 bytes, 32 bits)
    CRC32 (IEEE) of the 28 bytes above (4 bytes, 32 bits)
    """

    header = np.fromfile(input_filename, dtype=np.uint8, count=32)

    (
        sample_rate,
        center_frequency,
        start_time_stamp,
        sample_size,
        filler,
        crc32,
    ) = struct.unpack("<IQQIII", header.tobytes())

    meta = dict(
        sample_rate=sample_rate,
        center_frequency=center_frequency,
        start_time_stamp=start_time_stamp,
        sample_size=sample_size,
        filler=filler,
        crc32=crc32,
    )

    if sample_size == 16:
        config = {"dtype": np.int16, "scale": 0xFFFF}
    elif sample_size == 24:
        config = {"dtype": np.int32, "scale": 0xFFFFFF}
    else:
        raise Exception(f"Sample rate {sample_size} is not supported")

    data = np.fromfile(input_filename, dtype=config["dtype"], offset=32)
    float_data = data.astype(np.float32) / config["scale"]

    return float_data, meta


def I_signal(data: np.array):
    return data[:, 0]


def Q_signal(data: np.array):
    return data[:, 1]


def save_complex(data: np.array, output_filename: str):
    data.astype(np.float32).tofile(output_filename)
