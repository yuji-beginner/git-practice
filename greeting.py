class Greeting: 
    message = ""

    def __init__(self,greeting):
        self.message = greeting

    def greet(self):
        print(self.message)
    
if __name__ == "__main__":
    japanese = Greeting("こんにちは")
    japanese.greet()