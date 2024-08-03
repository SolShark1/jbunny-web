<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JBunny & Boosey</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        #kissMessage {
            display: none;
            margin-top: 20px;
            font-size: 24px;
            color: red;
        }
        .hidden {
            display: none;
        }
        .visible {
            display: block;
        }
        #cryptoEarned {
            margin-top: 20px;
            font-size: 20px;
            color: green;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Meme Coin Love Story!</h1>
    <p>
        Tap the button below to make JBunny and Boosey kiss.
    </p>
    <button id="kissButton">Make JBunny kiss Boosey</button>
    <div id="kissMessage">💖 JBunny and Boosey just kissed! 💖<br>The Meme Coin Love Story is coming true! 🌟</div>
    <div id="cryptoEarned" class="hidden">You have earned 10 Crypto!</div>
    <img id="giftsImage" src="path_to_your_gifts_image.png" alt="Gifts" class="hidden" style="width: 200px; height: auto; margin-top: 20px;">

    <script>
        document.getElementById('kissButton').addEventListener('click', function() {
            document.getElementById('kissMessage').style.display = 'block';
            document.getElementById('cryptoEarned').classList.remove('hidden');
            document.getElementById('giftsImage').classList.remove('hidden');
        });
    </script>
</body>
</html>