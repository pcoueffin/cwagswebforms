
<h1>Sorry, there's been an error. Please click on your dog's name.</h1>

<table border="1">
%hdr=None
%for row in rows:
  %if not hdr:
  %  hdr=row.keys()
  <tr>
    %for key in hdr:
      <th>{{key.title()}}</th>
    %end
  </tr>
  %end
  <tr>
    %for col in hdr:
    <td><a href="http://cwags.pythonanywhere.com/dog/{{row[col]}}">{{row[col]}}</a></td>
    %end
  </tr>
%end
</table>
