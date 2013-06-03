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
	</head>
	<body>
		<div id="wrap2">
			<div id="chat">	
				<div class="navblock">
					<div class="title-text">Chat</div>
					<div class="user-block"><span id="welcome-message"></span>
						<a href="/auth/logout" id="logoutbtn" class="btn" >Logout</a>
					</div>
				</div>		
				<form method="post" action="/chat">
					Message:<br />
					<textarea name="message" class="input-xlarge" rows="4"></textarea><br />
					<input type="submit" value="Send message" class="btn" />
				</form>
			</div>
			<div id="messages">
			</div>
		</div>
	</body>
</html>