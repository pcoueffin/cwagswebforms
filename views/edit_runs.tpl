<h1>Results so far:</h1>
<table border='0'>
%for row in results[0]:
    <tr>
      <td> {{row['name']}}</td>
      <td> {{row['level']}}</td>
      <td>{{row['result']}}</td>
    </tr>
%end

<form action="{{action}}" method="POST">
<table border="0">

  <tr>
     <td>Event date: </td>
      <td>Level: </td>
      <td>Round number: </td>
      </tr>
  %for row in results[1]:


    <tr>
      <td> {{row['date']}}</td>
      <td> {{row['level']}}</td>
      <td>{{row['idx']}}</td>
      <td>
	<input type="checkbox"  size="0" id="7" name="{{row['id']}}" value="{{row['id']}}"/>
      </td>
    </tr>

%end
</table>

<input type="submit" name="save" value="save">
</form>
