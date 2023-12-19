import datetime
import logging
import azure.functions as func

app = func.FunctionApp()


@app.schedule(
    schedule="0 * * * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False
)
def timer_trigger(myTimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.now(tz=datetime.timezone.utc).isoformat()

    if myTimer.past_due:
        logging.info("The timer is past due!")

    logging.info(f"Python timer trigger function executed. {utc_timestamp}")
