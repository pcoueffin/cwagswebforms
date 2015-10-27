
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

    <td><a href="http://cwags.pythonanywhere.com/dog/{{row['id']}}">{{row['name']}}</a></td>

  </tr>
%end
</table>
