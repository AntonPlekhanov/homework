class Logger:
    instance = None
    # l = []

    def __new__(cls, *args, **kwargs):
        # l = []
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            # l.append(cls.instance)
            cls.instance.l = []
        return cls.instance


    def log(self, message: str):
        self.l.append(message)
        print('ok')
    
    def get_logs(self):
        return self.l


logger1 = Logger()
logger2 = Logger()
print(logger1 is logger2)

logger1.log("First message")
logger2.log("Second message")

# print(logger1.get_logs())  
# print(logger2.get_logs()) 

# logger1.get_logs()
# logger2.get_logs()

assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["First message", "Second message"]



