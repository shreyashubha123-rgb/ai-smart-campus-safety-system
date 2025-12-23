def process_voice_command(command):
    """
    Voice-based campus assistant logic.
    """
    command = command.lower()

    if "library" in command:
        return "Go straight and turn right to reach the library."

    elif "medical" in command:
        return "The medical room is located near the main gate."

    elif "help" in command or "emergency" in command:
        return "Emergency alert has been sent to campus security."

    else:
        return "Sorry, I could not understand your request."
