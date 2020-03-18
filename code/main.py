from sql import *
from config import loads
from VkAPI import VkAPI

vk = VkAPI()

vk.messages.send(
    peer_id=447532348,
    message='hello',
    random_id=0
)

for event in vk:

    if event.type == 'message_new':

        print(event.object)
        vk.messaes.send(
            peer_id=447532348,
            message='hello, ' + str(event.object.message.from_id),
            random_id=0
        )
