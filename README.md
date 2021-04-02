# Check doctors availablitiy

This software automatically checks docs availability on this [website](https://servizi.apss.tn.it/ricmedico/)

## Configuration

Before running the program fill the fields

* `receiver`
* `senderEmailAddress`
* `senderPassword`

of the file `ustils/config.py`. To choose the doctor to monitor modify the field `doctorCodes` of the same file.

## Run

Install Docker and do the following:

* build the project with `make build`
* run it with `make run`
  