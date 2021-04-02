
receiver="put_email_where_you_want_to_receive_notifications"
senderEmailAddress = "put_email_server_used_to_send_email_notification"
senderPassword = "put_email_server_password"
subject = "Doctor availability"
#list of doctors: name of your choice, code of the doctor on the apss.tn.it website
doctorCodes = {
    "Dematte": 12981, 
    "Marra": 15084
}
baseURL = "https://servizi.apss.tn.it/ricmedico/medico.php?codMedicoMg="
sleepMinutes = 10