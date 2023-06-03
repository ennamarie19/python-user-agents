#!/usr/bin/env python3
import atheris
import sys
import fuzz_helpers


with atheris.instrument_imports():
    from user_agents import parse
def TestOneInput(data):
    fdp = fuzz_helpers.EnhancedFuzzedDataProvider(data)
    user_agent = parse(fdp.ConsumeRemainingString())
    user_agent.is_mobile
    user_agent.is_tablet
    user_agent.is_touch_capable
    user_agent.is_pc
    user_agent.is_bot
    str(user_agent)
def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
