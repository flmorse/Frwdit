#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", None)
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", 12345)
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "1AZWarzcBu7LLiILKupeQqIAZmqEUnSGHa8e1dU7HLAM_l5KkuqGUO26qnu6WcN71SfrIpnnHQ2Qn4bimR-k3w0IpSb8TlR8K74HmSMpZwrMTy8IVUjm04-tT4RHJ31LPNEfZf_-ZY8CQ5sd8rgsqJjf_Xc6o1rLylDdJLGpVuZETofiyODFl69cCacISHdT0pbaO2meTvzk3M0i-GG5rIMTdw-nOOnyv_wiReraEDA6UbJH0_nZQaNQvtW06dksFXV8X7q74lHfz7eNaMzeDNFU_CMQkmF7qMpxTNzmLARsTbBTc3XA5OpRkZf1vVJUizZ8xcQh3sUIqAh-E5reXZ6UL7LeWNl0=")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", 12345))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
