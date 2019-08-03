#!/usr/bin/env python3

from fronius2mqtt import config
from fronius2mqtt import daemon

def main():
	cfg = config.Config()
	cfg.read()
	d = daemon.Daemon(cfg)
	d.run()
	
main()

