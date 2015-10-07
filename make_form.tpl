%#template to generate a HTML form from a list of tuples 
%#(or list of lists, or tuple of tuples or ...)
<form action="{{action}}" method="POST">
  <table border="0">
    %hdr=None
    %for row in rows:
    %  if not hdr:
    %    hdr=row.keys()
    %  end
    %  for col in hdr:
    <tr>
      <td>{{col.title()}}</td>
      <td>
	<input type="text" size="10" name="{{col}}" 
	       value="{{row[col]}}"/>
      </td>
    </tr>
    %  end
    %end
  </table>
  <input type="submit" name="save" value="save">
</form>
