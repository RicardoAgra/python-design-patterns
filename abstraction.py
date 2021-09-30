from dataclasses import dataclass

@dataclass
class EmailService:
    #
    # Connected is an internal variable, therefor it should be set
    # to private.
    #
    _connected: bool = False

    def send_email(self):
        self._connect()
        print("Email sent")
        self._disconnect()

    #
    # Connect and Disconnect methods are only for internal use
    # and should be set as private to reduce complexity
    #

    def _connect(self) -> None:
        self._connected = True
        print("Connected")

    def _disconnect(self) -> None:
        self._connected = False
        print("Disconnected")

if __name__ == "__main__":
	print('Encapsulation')

	emailer = EmailService()
	emailer._disconnect()
	emailer._connect()
