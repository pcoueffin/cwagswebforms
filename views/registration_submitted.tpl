<h1> You've registered on the database!</h1>
this has changed
%for row in verify:
  %  hdr=row.keys()
  %print hdr
   <tr>
      %for key in hdr:
      <th>{{key.title()}}</th>
      %end
  </tr>

  <tr>
  %for key in hdr:
  <td>{{row[key]}}</td>
  %end
  </tr>