%#template to generate a HTML form from a list of tuples 
%#(or list of lists, or tuple of tuples or ...)



<form action="{{action}}" method="POST">

  <div class="form-all">
    <ul class="form-section page-section">
%names=results[0]
  %row=results[1][0]
  %for (elt, name) in zip(row, names):
%if name[0]== "datatype":
%datatype = elt
%elif name[0] == "dataid":
%dataid = elt
%elif name[0] == "dataname":
%dataname = elt
%else:
%pass
    %end
%end
 <li class="form-line" data-type={{datatype}} id=id_{{dataid}}>
        <label class="form-label form-label-left form-label-auto" id="label_{{dataid}}" for="input_1"> {{dataname.title()}} </label>
            <input class="form-textbox" type="text" size="10" name="{{dataname}}" id="{{dataid}}" />
        </div>
      </li>
      <li class="form-line" data-type="control_button" id="id_2">
        <div id="cid_2" class="form-input-wide">
          <div style="margin-left:156px" class="form-buttons-wrapper">
            <button id="input_2" type="submit" class="form-submit-button">
              Submit
            </button>
          </div>
        </div>
      </li>
    </ul>
  </div>
<input type="submit" name="save" value="save">
</form>