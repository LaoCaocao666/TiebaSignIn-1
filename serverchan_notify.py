#!/usr/bin/env python3
"""Server 酱推送模块"""

import logging
import os
import urllib.parse
import urllib.request

logger = logging.getLogger(__name__)


def send_markdown(content: str, title: str = "贴吧签到结果") -> None:
    """通过 Server 酱推送。未配置 SCKEY 则自动跳过。"""
    sckey = os.environ.get("SCKEY", "").strip()
    if not sckey:
        logger.info("未配置 SCKEY，跳过 Server 酱推送")
        return
    url = f"https://sctapi.ftqq.com/{sckey}.send"
    data = urllib.parse.urlencode({"title": title, "desp": content}).encode()
    try:
        with urllib.request.urlopen(url, data=data, timeout=15) as resp:
            logger.info(f"Server 酱推送完成，HTTP {resp.status}")
    except Exception as e:
        logger.error(f"Server 酱推送失败: {e}")
