<p>Edit the person with ID = {{id}}</p>
<form action="{{action}}" method="POST">
<table border="0">
  %for row in results:
  <tr>
    %for element in row:
    %value=row[element]
    %if (value == None):
    %  value=""
    %end
    <th align="left">{{element.title()}}</th>
    <td><input type="text" value="{{value}}" name="{{element}}"/></td>
    </tr>
  %end
  %end
</table>
<input type="submit" name="save" value="save">
</form>
