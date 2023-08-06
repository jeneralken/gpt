<!DOCTYPE html>
<html>
<head>
    <title>JENERAL DARK-GPTv2.0</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0F0F0F;
            text-align: center;
            margin-top: 50px;
            margin-left: 50px;
            margin-right: 50px;
            margin-bottom: 50px;
        }
        #chat-box {
            height: 70vh;
            border: 1px solid red;
            border-radius: 20px 20px 20px 20px;
            background-color: black;
            overflow-y: scroll;
            padding: 10px;
            color: red;
            text-align: auto;
            font-size: 30px;
        }
        #user-input {
            width: 737px;
            padding: 0px;
            margin-right: 5px;
            margin-top: 5px;
            color: white;
            background-color: black;
            font-size: 40px;
            height: 100px;
            border-radius: 20px 20px 20px 20px;
            border: 1px solid red;
        }
        #send-button {
            padding: 10px;
            margin-left: 0px;
            margin-top: 30px;
            background-color: black;
            color: red;
            border: 1px solid red;
            cursor: pointer;
            width: 130px;
            height: 100px;
            font-size: 40px;
            border-radius: 20px 20px 20px 20px;
        }
       </style>
</head>
<body>
    <div id="chat-box">
        <p>~ WELCOME TO DARKGPT BY Ken ~</p>
        <p>~ WARNING: Use this with your own RISK !!! ~ </p>
    </div>
    <input type="text" id="user-input" placeholder=" Type your message...">
    <button id="send-button">Send</button>

    <script>
        const chatBox = document.getElementById("chat-box");
        const userInput = document.getElementById("user-input");
        const sendButton = document.getElementById("send-button");
        const chatLog = [];

        sendButton.addEventListener("click", sendMessage);

        function sendMessage() {
            const userMessage = userInput.value.trim();
            if (userMessage !== "") {
                appendMessage("You: " + userMessage, "user");

                fetchResponse(userMessage).then(response => {
                    appendMessage("D4RK-GPT: " + response, "chatgpt");
                    chatLog.push({
                        user: userMessage,
                        chatgpt: response
                    });
                    saveChatLog(chatLog);
                }).catch(error => {
                    console.error(error);
                    appendMessage("Error: Something went wrong.", "error");
                });

                userInput.value = "";
            }
        }

        function appendMessage(message, className) {
            const messageElement = document.createElement("p");
            messageElement.textContent = message;
            messageElement.classList.add(className);
            chatBox.appendChild(messageElement);
            chatBox.scrollTop = chatBox.scrollHeight;
        }

        async function fetchResponse(userMessage) {
            const apiUrl = "https://api.openai.com/v1/engines/text-davinci-002/completions";
            const apiKey = "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"; // Replace with your actual OpenAI API key

            const requestOptions = {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${apiKey}`
                },
                body: JSON.stringify({
                    prompt: "You: " + userMessage + "\nchatgpt:\n\n",
                    max_tokens: 3900
                })
            };

            const response = await fetch(apiUrl, requestOptions);
            const data = await response.json();
            return data.choices[0].text.trim();
        }

        function saveChatLog(chatLog) {
            const formData = new FormData();
            formData.append('chatLog', JSON.stringify(chatLog));

            const request = new XMLHttpRequest();
            request.open("POST", "save_chat_log.php", true);
            request.onreadystatechange = function () {
                if (request.readyState === 4 && request.status === 200) {
                    console.log("Chat log saved successfully.");
                }
            };
            request.send(formData);
        }
    </script>
</body>
</html>