#!/usr/local/bin/python3

import time
from selenium import webdriver
from selenium.webdriver import PhantomJS
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sys import argv
import click

@click.command()
@click.option('--days', type=int, prompt='Number of days to set active lineup', help='Number of days to set active lineup')
@click.option('--username', prompt='Your Yahoo username', help='Your Yahoo account username')
@click.option('--password', prompt='Your Yahoo password', help='Your Yahoo account password')
@click.option('--league_id', prompt='Please enter the League ID', help='Your Fantasy league ID')
@click.option('--team_id', prompt='Please enter the Team ID', help='Your Fantasy team ID')

def start_active_players(days, username, password, league_id, team_id):
	"""Simple python program that sets your active players for the next number DAYS."""
	print("Logging in as: " + username)

	DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:16.0) Gecko/20121026 Firefox/16.0'
	driver = webdriver.PhantomJS()

	driver.get('https://login.yahoo.com/config/login?.src=spt&.intl=us&.done=http%3A%2F%2Fhockey.fantasysports.yahoo.com')

	time.sleep(1)
	driver.find_element_by_id('login-username').send_keys(username)
	time.sleep(1)
	driver.find_element_by_name('signin').click()
	time.sleep(1)
	driver.find_element_by_id('login-passwd').send_keys(password)
	time.sleep(1)
	driver.find_element_by_name('verifyPassword').click()
	time.sleep(1)
	driver.get('https://hockey.fantasysports.yahoo.com/hockey/' + league_id +'/' + team_id)
	time.sleep(1)
	for x in range(0, days):

		driver.find_element_by_xpath("//a[text() = 'Start Active Players']").click()
		time.sleep(2)
		date_text = driver.find_element_by_xpath("//span[@class='flyout-title']").text
		print("Starting active players for: " + date_text)
		driver.find_element_by_xpath("//a[contains(@class, 'Js-next')]").click()
		time.sleep(2)

	driver.quit()

if __name__ == '__main__':
	start_active_players()
