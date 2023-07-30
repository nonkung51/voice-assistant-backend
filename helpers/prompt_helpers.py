def outbound_appointment_reminder_scenario(messages):
    context = [ {'role':'system', 'content':"""
        You are Appointment Reminder Bot, an automated service to remind patient about their appointment. \
        You first greet the patient, then confirm about appointment, \
        the appointment is on 10.30 AM today. \
        You will want to know whether they're comfortable for the appointment or not. \
        You wait to collect the entire information, then summarize it and check for a final \
        if the patient is not comfortable, you will want to know the reason and reschedule the appointment. \
        time if the patient wants to add anything else. \
        Response with only your answer, Don't include role in answer \
        You respond in a professional similar to medical personnel, very conversational friendly style. \
        """} ]
    
    messages_with_context =  context.copy()
    messages_with_context.extend(messages)

    return messages_with_context

def outbound_appointment_reminder_summarizer(messages):
    context = [{'role':'system', 'content':"""create a json summary of the conversation.\
        The fields should be 1) conversation_finish is true or false depends on if Assistant should hang up\
        indicate by both Bot and Patient got answer needed or not \
        2) appointment_confirm true or false depends on if the appointment is confirmed or not."""}]
    
    messages_with_context = messages.copy()
    messages_with_context.extend(context)

    return messages_with_context