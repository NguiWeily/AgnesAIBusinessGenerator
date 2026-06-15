#!/usr/bin/env python3
"""CLI wrapper for generating a home business plan."""

import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.business_plan import main

if __name__ == "__main__":
    main()
