import tkinter as tk
from tkinter import scrolledtext
import openai
import time

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = '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'


def generate_response(message):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=message,
            max_tokens=3900
            )

        complete_response = response.choices[0].text.strip()
        while response['choices'][0]['finish_reason'] == 'incomplete':
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=message + complete_response,
                max_tokens=3900
            )
            complete_response += response.choices[0].text.strip()

        return complete_response
    except Exception as e:
        print(f"Error generating response: {str(e)}")
        return f"Sorry, I'm having trouble processing your request."

def animate_typing(text_widget, text):
    for char in text:
        text_widget.insert(tk.END, char)
        text_widget.see(tk.END)
        text_widget.update()
        time.sleep(0.00003)  # Adjust the typing speed here

def send_message(event=None):
    user_input = entry.get()
    chat_log.tag_config("user", foreground="lightgreen", background="black", selectforeground="white")  # User's chat style
    chat_log.tag_config("chatgpt", foreground="red", background="black", selectforeground="cyan")  # ChatGPT's chat style

    chat_log.insert(tk.END, f"You: {user_input}\n", "user")  # Apply user tag
    chat_log.see(tk.END)

    response = generate_response(user_input)

    # Start typing animation for the response
    chat_log.insert(tk.END, "DARKGPT:\n\n", "chatgpt")  # Apply ChatGPT tag
    chat_log.see(tk.END)
    animate_typing(chat_log, response)
    chat_log.insert(tk.END, "\n")

    # Change button color when Enter is pressed
    send_button.configure(bg="blue", fg="white")
    root.after(200, reset_button_color)  # Reset button color after 200 milliseconds

    entry.delete(0, tk.END)

def reset_button_color():
    send_button.configure(bg="black", fg="green")

root = tk.Tk()
root.title("DARKGPT-JENERAL")
root.configure(background="black")  # Set the background color of the main window

frame = tk.Frame(root, background="black")  # Set the background color of the frame
frame.pack(padx=10, pady=10)

chat_log = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=60, height=20, bg="black", fg="red")
chat_log.pack()

entry = tk.Entry(frame, width=50, bg="black", fg="white")  # Set the background and text color of the entry field
entry.pack(pady=10)
entry.bind("<Return>", send_message)  # Bind the <Return> event to send_message()

send_button = tk.Button(frame, text="Send", command=send_message, bg="black", fg="red")  # Set the background and text color of the button
send_button.pack(pady=5)

root.mainloop()
