<!DOCTYPE html>
<html>
	<head>
		<title>Chat</title>
		<meta charset="utf-8" />
		<link href="/static/bootstrap/css/bootstrap.css" rel="stylesheet">
		<link href="/static/messenger/css/common.css" rel="stylesheet">
		<script type="text/javascript" src="/static/bootstrap/js/bootstrap.min.js"></script>
		<script type="text/javascript" src="/static/jquery/js/jquery-1.9.1.min.js"></script>
		<script type="text/javascript" src="/static/jquery/js/jquery.cookie.js"></script>
		<script type="text/javascript" src="/static/messenger/js/common.js"></script>
		<script type="text/javascript">
			setTimeout(updateChat, 1000);

			function updateChat() {
    			$.post(
					'/chat/list', 
					{
					},
					function (data) {
						update_messages(data.messages);
						update_online_users(null);
					},
					'json'
				);
    			setTimeout(updateChat, 1000);
			}		
		</script>
	</head>
	<body>
		<div id="wrap2">
			<div class="navblock">
					<div class="title-text">Chat</div>
					<div class="user-block"><span id="welcome-message"></span>
						<a href="/auth/logout" id="logoutbtn" class="btn" >Logout</a>
					</div>
				</div>		
			<div id="chat">	
				<div class="fetched-content">	
					<div id="messages">
					</div>
					<div id="online-users">
					</div>
				</div>
				<div class="controls-content">		
					<form method="post" action="/chat">
						<textarea name="message" class="message-input" rows="1" wrap="off"></textarea>
						<input type="submit" value="Send message" class="btn" id="btn" />
					</form>
				</div>
			</div>
		</div>
	</body>
</html>