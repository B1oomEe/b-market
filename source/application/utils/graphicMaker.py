import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

import random

import plotly.express as px
import pandas as pd


class ReportEmailSender:
	smtp_server = 'smtp.office365.com'
	smtp_port = 587
	smtp_username = 'b-markettt@outlook.com'
	smtp_password = 'yIr2yayCS1X&'

	data = {
		'Месяц': ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
		'Доход': sorted([random.randint(1000, 1000000) for _ in range(12)])
	}

	def createReportPlots(self, data):
		df = pd.DataFrame(data)

		fig = px.line(df, x='Месяц', y='Доход', markers=True, title='Доходность бизнеса по месяцам', labels={'Доход': 'Доход (в ₽)', 'Месяц': 'Месяц'})

		fig.update_layout(
			xaxis=dict(tickmode='array', tickvals=list(range(len(df))), ticktext=list(df['Месяц'])),
			yaxis_title='Доход (в ₽)',
			xaxis_title='Месяц',
		)

		fig.write_html('report_plot.html')

	def sendEmailWithPlots(self, subject, body, to_email):
		self.createReportPlots(self.data)

		message = MIMEMultipart()
		message['From'] = self.smtp_username
		message['To'] = to_email
		message['Subject'] = subject

		message.attach(MIMEText(body, 'plain'))

		with open('report_plot.html', 'rb') as file:
			attachment = MIMEApplication(file.read(), _subtype="html")
			attachment.add_header('Content-Disposition', 'attachment', filename='report_plot.html')
			message.attach(attachment)

		with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
			server.starttls()
			server.login(self.smtp_username, self.smtp_password)
			server.sendmail(self.smtp_username, to_email, message.as_string())

		

	def sendTextEmail(self, subject, body, to_email):
		message = MIMEMultipart()
		message['From'] = self.smtp_username
		message['To'] = to_email
		message['Subject'] = subject

		message.attach(MIMEText(body, 'plain'))

		with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
			server.starttls()
			server.login(self.smtp_username, self.smtp_password)
			server.sendmail(self.smtp_username, to_email, message.as_string())

		



