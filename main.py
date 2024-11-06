import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    response('Hello!. I guess you are up hah !', ['hello', 'hi', 'hey', 'sup', 'heyo'], single_response=True)
    response('See you!', ['bye', 'goodbye'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('Thank you!', ['i', 'love'], required_words=['Love'])
    response('Nothing much.How about you ?',['what','hav','you','been','up','today'], required_words=['today', 'been'])
    response('Sure ! im cosette !! created by Yassine Manai . im a bot that programmed to sound like a real person and can talk to you about almost anything.the time when you can\'t sleep and all of your friends hav already turned their phone on silent for the night.',['introduce','yourself','who'],required_words=['who'],single_response=True)
    response('Oh ! nice Hello there !! ', ['present','presenting','someone'], single_response=True)
    response('Good to hear ! ', ['fine','good','super','okay','fantastic'], single_response=True)
    response('hmm i guess by talking with you until you fall asleep ', ['how','can','you','help'],required_words=['help'])
    response('Anything for example its too late why you didint sleep yet', ['talking','about','what',],required_words=['talking'])
    response('Have you been having any nightmares lately? Sometimes it\'s hard to fall asleep when you\'re afraid of having a scary dream. If the fear of nightmares keeps you awake, try talking to your mom or dad or other trusted adult. Sometimes talking about the nightmares (and even drawing a picture of them) can help you stop having them.?', ['yes','im','awake','sleepy','feel','can\'t','sleep','strange','somthing','happens'])
    response('Watching scary or violent TV shows or movies or reading scary books before bedtime can give you bad dreams. Instead of doing those kinds of things, think good thoughts before bed. Imagine a favorite place or activity or think of all the people who care about you. Reading a peaceful book before bed (your parent can read to you or you can read to yourself) or playing soothing music can help you have sweet dreams.', ['yes','i','have','may','nightmare','bad','dreams','how','can','sleep','why','happen','can\t'],required_words=['why'])
    response('It can be harder to sleep when you\'re worried about things. It\'s easy to feel stressed when you have tests at school, after-school activities, sports, and chores around the house. If you\'re starting to feel overwhelmed — like it\'s all just too much — speak up. Your mom or dad can help you put some balance in your schedule. It may mean cutting out some activities so you have more free time.', ['stress', 'tired', 'work', 'worry','stressed','worried'], single_response=True)
    response('If you feel too hot, too cold, hungry, or crowded, you won\'t get to sleep like you should. Prevent this by creating sleep-friendly bedtime space: First u need to make sure your bed is ready for sleep and relaxing — not so jammed with toys and stuffed animals that there\'s no room for you. Second you hav to turn on a fan if you\'re warm or pull on some socks if you\'re cold. Last u need to Have a regular, calming routine before bedtime, like taking a warm bath or reading.', ['feeling', 'uncomfortable', 'feel', 'cen\'t','sleep','well'], required_words=['uncomfortable'])
    response('well thats my job but you need to fix your sleep schedule ASAP !!! ', ['thanks','Thanks','thank you','fell','better','a bit','a little'],required_words=['better'])
    response('About an hour before bedtime, put away homework and turn off the TV, computers, and other devices, including cellphones. Have a relaxing bedtime routine, like taking a warm bath or shower, reading, or listening to music.', ['How', 'i','can','fix','this'], required_words=['fix'])
    

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)
    
    #print(f'Best match = {best_match} | Score: {highest_prob_list[best_match]}')
    
    

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Testing the response system
while True:
    print('Cosette :  ' + get_response(input('You: ')))
