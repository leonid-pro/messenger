<!DOCTYPE html>
<html>
	<head>
		<title>Chat</title>
		<meta charset="utf-8" />
		<style type="text/css">
			body {
				margin: 0;
				padding: 0;
				font-family: Arial, sans-serif;
				font-size: 13px;
			}
			#wrap {
				width: 1000px;
				margin: 20px auto;
			}
			
			.message-item {
				margin: 20px 0;
			}
			
		</style>
	</head>
	<body>
		<div id="wrap">		
		
			<div id="send-message">			
				<form method="post" action="/chat/put-message">
					Message:<br />
					<textarea name="message"></textarea><br />
					<input type="submit" value="Send" />
				</form>
			</div>
			
			<div id="messages">
				<div class="message-item">
					<div class="from">Alexander Navka</div>
					<div class="datetime">2013-03-03 12:12</div>
					<div class="message-text">Test</div>
				</div>
			</div>
		</div>
	</body>
</html>