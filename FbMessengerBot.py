from fbchat import log, Client
from fbchat.models import *
from win32com.client import Dispatch


class Shomik(Client):
    def speak(self, str):
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(str)

    def onMessage(self, mid=None, author_id=None, message=None, message_object=None,
                  thread_id=None, thread_type=ThreadType.USER, ts=None, metadata=None, msg=None,
                  ):
        log.info("Message {} from {} in {}".format(message_object, thread_id, thread_type))
        reply = "Hello! there I am not available right now." \
                " Please Leave Your Message. I will reply you soon In Sha Allah. Have a great Time"
        client.speak("Hello sir! There is a new Message. Please Check it out")

        try:
            ls = client.fetchGroupInfo(thread_id)
        except Exception as e:
            if author_id != self.uid:
                self.send(Message(text=reply), thread_id=thread_id, thread_type=thread_type)
                self.markAsUnread(thread_ids=thread_id)
                self.markAsDelivered(author_id, thread_id)


client = Shomik("********.com", "****")
client.listen()
