import pathlib

PACKAGE_NAME = str(pathlib.Path(__file__).parent).split("\\")[-1]

INVOKE_NAME = "TimeMe"

COMMANDS = {
    "new" : "timeme.TIMERS.new_timer('{}')\n",
    "start" : "timeme.TIMERS.start_timer('{}')\n",
    "stop" : "timeme.TIMERS.stop_timer('{}')\n",
    "print" : "timeme.TIMERS.print_timer('{}')\n"
}

STATIC = {
    "printall" : "print(timeme.TIMERS)\n",
    "import" : "import timeme\n"
}