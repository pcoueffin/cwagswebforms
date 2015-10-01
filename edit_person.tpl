<p>Edit the person with ID = {{id}}</p>
<form action="{{action}}" method="POST">
<table border="0">
  %names=results[0]
  %row=results[1]
  %for (elt, name) in zip(row, names):
    <tr>
      <th align="left">{{name[0].title()}}</th>
      <td><input type="text" name="{{name[0]}}" value="{{elt}}"/></td>
    </tr>
  %end
</table>
<input type="submit" name="save" value="save">
</form>
