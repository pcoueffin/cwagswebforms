%#template to generate a HTML form from a list of tuples 
%#(or list of lists, or tuple of tuples or ...)

<form action="{{action}}" method="POST">
  <table border="0">
    %hdr=None
    %for row in rows:
    <tr>
      <td>{{row['dataname'].title()}}</td>
      <td>
	<input type="{{row['datatype']}}"  size="{{row['datalength']}}" id="{{row['dataid']}}"/>
      </td>
    </tr>
    %end
  </table>
  <input type="submit" name="submit" value="save">
</form>
