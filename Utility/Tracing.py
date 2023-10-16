#trace.playwright.dev

from playwright.sync_api import BrowserContext

class Tracing_the_test:

    def __init__(self, browser_context :BrowserContext):
        self.browser_context = browser_context
   
    def Start_Trace_test(self):
       self.browser_context.tracing.start(
        name="signup_trace",
        screenshots=True,
        snapshots=True,
        sources=True,
    )
    
    def Stop_Trace_test(self):
       self.browser_context.tracing.stop(path="QAtrace.zip")

