# Author: Hongwei Fan(@hwfan)
# Date: Dec 25, 2019
# Last Update: Sep 13, 2020
from DriveDownloader.netdrive_helpers.gd_helper import gd_download
from DriveDownloader.netdrive_helpers.od_helper import od_download
import argparse
import os
def parse_args():
    parser = argparse.ArgumentParser(description='Drive Downloader Args')
    parser.add_argument('url', help='URL you want to download from.', default='', type=str)
    parser.add_argument('--filename', help='Target file name.', default='', type=str)
    parser.add_argument('--proxy', help='Proxy address when needed.', default='', type=str)
    args = parser.parse_args()
    return args

def simple_cli():
    args = parse_args()
    assert len(args.url) > 0

    print('============ Drive Downloader V1.2 ============')
    if '1drv.ms' in args.url or '1drv.ws' in args.url:
        download_api = od_download
    elif 'drive.google.com' in args.url:
        download_api = gd_download
    else:
        raise NotImplementedError("The drive type is not supported!")
    final_proxy = args.proxy.strip() if len(args.proxy)>0 else None
    download_api(args.url.strip(), args.filename.strip(), final_proxy)

if __name__ == '__main__':
    cli()