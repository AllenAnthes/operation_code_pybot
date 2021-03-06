from slackclient import SlackClient
from decouple import config

TOKEN = config('OPCODE_APP_TOKEN')

slack_client = SlackClient(TOKEN)


def list_channels():
    channels_call = slack_client.api_call("channels.list")
    if channels_call.get('ok'):
        return channels_call['channels']
    return None


def channel_info(channel_id):
    info = slack_client.api_call("channels.info", channel=channel_id)
    if info:
        return info['channel']
    return None


def send_message(channel_id, message):
    slack_client.api_call(
        "chat.postMessage",
        channel=channel_id,
        text=message,
        username='test-bot',
        icon_emoji=':robot_face:'
    )


if __name__ == '__main__':
    channels = list_channels()
    if channels:
        print("Channels: ")
        for channel in channels:
            print(channel['name'] + " (" + channel['id'] + ")")
            # detailed_info = channel_info(channel['id'])
            # if detailed_info:
            #     if detailed_info['members']:
            #         print([x for x in detailed_info['members']])
            # print('Latest text from ' + channel['name'] + ":")
            # print(detailed_info['latest']['text'])
        print('-----')
    else:
        print("Unable to authenticate.")
