<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1> Hello JSP </h1>
   <h2> Scripting Tag</h2>
   <%! int count=3; 
       String makeItLower(String data) {
          return data.toLowerCase();
       }
   %>
   <%
       for( int i=1; i<= count; i++){
          out.println( i + "<br>");
       }
   %>
   <%= makeItLower("Hi!") %> 
	
</body>
</html>