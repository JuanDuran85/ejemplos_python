# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_

Returns:
    _type_: _description_
"""

import speedtest


def get_internet_speed() -> dict[str, float | int]:
    """
    Measures the internet speed by testing download and upload speeds and ping.

    Returns:
        tuple[float, float, int]: A tuple containing download speed in Mbps, 
        upload speed in Mbps, and ping in ms.
    """

    st: speedtest.Speedtest = speedtest.Speedtest()
    download_fn: float = st.download() / 1024 / 1024
    upload_fn: float = st.upload() / 1024 / 1024
    ping_fn: int = st.results.ping
    return {"download": download_fn, "upload": upload_fn, "ping": ping_fn}


if __name__ == "__main__":
    result: dict[str, float | int] = get_internet_speed()
    print(f"Download: {result["download"]:.2f} Mbps")
    print(f"Upload: {result["upload"]:.2f} Mbps")
    print(f"Ping: {result["ping"]:.2f} ms")
