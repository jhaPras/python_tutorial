{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "import pandas as pd\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from selenium import webdriver\n",
    "from splinter import Browser\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "### Activating browser in selenium and the browser we are using is Chrome\n",
    "\n",
    "spirit_browser = webdriver.Chrome('/usr/local/bin/chromedriver 2')\n",
    "spirit_browser.get('https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest')\n",
    "\n",
    "\n",
    "\n",
    "## Beautiful Soup object \n",
    "\n",
    "doc_obj = bs(spirit_browser.page_source,'html.parser')\n",
    "\n",
    "\n",
    "\n",
    "## This part extracts title information from the page and as it fetches all the 'content title' tags, it is limited\n",
    "## to first 40 elements\n",
    "\n",
    "title = doc_obj.find_all('div',{'class':'content_title'})\n",
    "title_list = [t.get_text().replace('\\n','') for t in title][:40]\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "## this part extracts paragraph text from the page and stores it into variable\n",
    "\n",
    "\n",
    "paragraph_text = doc_obj.find_all('div',{'class':'article_teaser_body'})\n",
    "paragraph_text_list = [t.get_text() for t in paragraph_text]\n",
    "\n",
    "\n",
    "spirit_browser.quit()\n",
    "\n",
    "\n",
    "## debug statement to check the length of both lists if they are equal\n",
    "print(len(title_list)==len(paragraph_text_list)) \n",
    "\n",
    "\n",
    "##we will be adding the data to dataframe and we will add elements further \n",
    "data = {\n",
    "    'title':title_list,\n",
    "    'title_text':paragraph_text_list\n",
    "}\n",
    "\n",
    "my_obj = pd.DataFrame(data)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "### Handler code for images \n",
    "\n",
    "\n",
    "image_browser = webdriver.Chrome('/usr/local/bin/chromedriver 2')\n",
    "image_browser.get('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')\n",
    "\n",
    "\n",
    "\n",
    "## Beautiful Soup object \n",
    "\n",
    "doc_obj = bs(image_browser.page_source,'html.parser')\n",
    "\n",
    "\n",
    "\n",
    "images = image_browser.find_elements_by_class_name('thumb')\n",
    "images_link = [t.get_attribute('src') for t in images][:32]\n",
    "\n",
    "date_list = doc_obj.find_all('h3',{'class':'release_date'})\n",
    "release_dates = [d.get_text() for d in date_list]\n",
    "\n",
    "headlines = doc_obj.find_all('div',{'class':'item_tease_overlay'})\n",
    "headline = [h.get_text() for h in headlines]\n",
    "\n",
    "\n",
    "image_browser.quit()\n",
    "\n",
    "\n",
    "\n",
    "data = {'photo_title':headline,\n",
    "        'date_realeased':release_dates,\n",
    "        'image_link':images_link}\n",
    "\n",
    "pd_obj = pd.DataFrame(data)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>photo_title</th>\n",
       "      <th>date_realeased</th>\n",
       "      <th>image_link</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Olympia Undae</td>\n",
       "      <td>November 7, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>InSight's Arm Camera Stares Into the Pit</td>\n",
       "      <td>November 6, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Micoud Crater</td>\n",
       "      <td>November 6, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Terraced Wall Crater</td>\n",
       "      <td>November 5, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Lyot Crater Dunes</td>\n",
       "      <td>November 4, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Chincoteague Crater</td>\n",
       "      <td>November 1, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Nili Fossae</td>\n",
       "      <td>October 31, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Aromatum Chaos</td>\n",
       "      <td>October 30, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Medusae Fossae</td>\n",
       "      <td>October 29, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Idaeus Fossae</td>\n",
       "      <td>October 28, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>InSight's Heat Probe Partially Backs Out of Hole</td>\n",
       "      <td>October 28, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Indus Vallis</td>\n",
       "      <td>October 25, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Curiosity at Glen Etive</td>\n",
       "      <td>October 24, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Dark Slope Streaks</td>\n",
       "      <td>October 24, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Indus Vallis Tributaries</td>\n",
       "      <td>October 23, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Hephaestus Fossae</td>\n",
       "      <td>October 22, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Enigmatic Canyon Dunes</td>\n",
       "      <td>October 21, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Pristine Dust Deposits in Syria Planum</td>\n",
       "      <td>October 21, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Down in Chukhung Crater</td>\n",
       "      <td>October 21, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>A Martian Game Board</td>\n",
       "      <td>October 21, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Athabasca Valles</td>\n",
       "      <td>October 21, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Uranius Fossae</td>\n",
       "      <td>October 18, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Pinning Helps the Mole Move</td>\n",
       "      <td>October 17, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Elysium Fossae</td>\n",
       "      <td>October 17, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>HiRISE Watches Curiosity Journey Across the Cl...</td>\n",
       "      <td>October 16, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>The Best View of InSight</td>\n",
       "      <td>October 16, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>Cerberus Fossae</td>\n",
       "      <td>October 16, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>Arabia Terra Channel</td>\n",
       "      <td>October 15, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Olympica Fossae</td>\n",
       "      <td>October 14, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>Terra Cimmeria</td>\n",
       "      <td>October 11, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>Lyot Crater Dunes</td>\n",
       "      <td>October 10, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>Cerulli Crater Rim</td>\n",
       "      <td>October 9, 2019</td>\n",
       "      <td>https://www.jpl.nasa.gov/spaceimages/images/wa...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                          photo_title    date_realeased  \\\n",
       "0                                       Olympia Undae  November 7, 2019   \n",
       "1            InSight's Arm Camera Stares Into the Pit  November 6, 2019   \n",
       "2                                       Micoud Crater  November 6, 2019   \n",
       "3                                Terraced Wall Crater  November 5, 2019   \n",
       "4                                   Lyot Crater Dunes  November 4, 2019   \n",
       "5                                 Chincoteague Crater  November 1, 2019   \n",
       "6                                         Nili Fossae  October 31, 2019   \n",
       "7                                      Aromatum Chaos  October 30, 2019   \n",
       "8                                      Medusae Fossae  October 29, 2019   \n",
       "9                                       Idaeus Fossae  October 28, 2019   \n",
       "10   InSight's Heat Probe Partially Backs Out of Hole  October 28, 2019   \n",
       "11                                       Indus Vallis  October 25, 2019   \n",
       "12                            Curiosity at Glen Etive  October 24, 2019   \n",
       "13                                 Dark Slope Streaks  October 24, 2019   \n",
       "14                           Indus Vallis Tributaries  October 23, 2019   \n",
       "15                                  Hephaestus Fossae  October 22, 2019   \n",
       "16                             Enigmatic Canyon Dunes  October 21, 2019   \n",
       "17             Pristine Dust Deposits in Syria Planum  October 21, 2019   \n",
       "18                            Down in Chukhung Crater  October 21, 2019   \n",
       "19                               A Martian Game Board  October 21, 2019   \n",
       "20                                   Athabasca Valles  October 21, 2019   \n",
       "21                                     Uranius Fossae  October 18, 2019   \n",
       "22                        Pinning Helps the Mole Move  October 17, 2019   \n",
       "23                                     Elysium Fossae  October 17, 2019   \n",
       "24  HiRISE Watches Curiosity Journey Across the Cl...  October 16, 2019   \n",
       "25                           The Best View of InSight  October 16, 2019   \n",
       "26                                    Cerberus Fossae  October 16, 2019   \n",
       "27                               Arabia Terra Channel  October 15, 2019   \n",
       "28                                    Olympica Fossae  October 14, 2019   \n",
       "29                                     Terra Cimmeria  October 11, 2019   \n",
       "30                                  Lyot Crater Dunes  October 10, 2019   \n",
       "31                                 Cerulli Crater Rim   October 9, 2019   \n",
       "\n",
       "                                           image_link  \n",
       "0   https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "1   https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "2   https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "3   https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "4   https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "5   https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "6   https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "7   https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "8   https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "9   https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "10  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "11  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "12  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "13  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "14  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "15  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "16  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "17  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "18  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "19  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "20  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "21  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "22  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "23  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "24  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "25  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "26  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "27  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "28  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "29  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "30  https://www.jpl.nasa.gov/spaceimages/images/wa...  \n",
       "31  https://www.jpl.nasa.gov/spaceimages/images/wa...  "
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# pd_obj"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>title</th>\n",
       "      <th>title_text</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NASA's Mars 2020 Heads Into the Test Chamber</td>\n",
       "      <td>In this time-lapse video taken at JPL, enginee...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Screening Soon: 'The Pathfinders' Trains Lens ...</td>\n",
       "      <td>With the Mars 2020 mission ramping up, the doc...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>InSight's 'Mole' Team Peers into the Pit</td>\n",
       "      <td>Efforts to save the heat probe continue.</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Common Questions about InSight's 'Mole'</td>\n",
       "      <td>There's a new plan to get InSight's \"mole\" mov...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Mars 2020 Stands on Its Own Six Wheels</td>\n",
       "      <td>In time-lapse video, taken at JPL, captures th...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>New Selfie Shows Curiosity, the Mars Chemist</td>\n",
       "      <td>The NASA rover performed a special chemistry e...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Naming a NASA Mars Rover Can Change Your Life</td>\n",
       "      <td>Want to name the robotic scientist NASA is sen...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Mars 2020 Unwrapped and Ready for More Testing</td>\n",
       "      <td>In time-lapse video, bunny-suited engineers re...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>HiRISE Views NASA's InSight and Curiosity on Mars</td>\n",
       "      <td>New images taken from space offer the clearest...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>NASA's Curiosity Rover Finds an Ancient Oasis ...</td>\n",
       "      <td>New evidence suggests salty, shallow ponds onc...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>NASA's Mars 2020 Rover Tests Descent-Stage Sep...</td>\n",
       "      <td>A crane lifts the rocket-powered descent stage...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>NASA's Push to Save the Mars InSight Lander's ...</td>\n",
       "      <td>The scoop on the end of the spacecraft's robot...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>NASA's InSight 'Hears' Peculiar Sounds on Mars</td>\n",
       "      <td>Listen to the marsquakes and other, less-expec...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>NASA Mars Mission Connects With Bosnian and He...</td>\n",
       "      <td>A letter from NASA was presented to the mayor ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Deadline Closing for Names to Fly on NASA's Ne...</td>\n",
       "      <td>You have until Sept. 30 to send your names to ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>NASA Wins Two Emmy Awards for Interactive Miss...</td>\n",
       "      <td>NASA-JPL's coverage of the Mars InSight landin...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>NASA's Mars 2020 Comes Full Circle</td>\n",
       "      <td>Aiming to pinpoint the Martian vehicle's cente...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>NASA Invites Students to Name Mars 2020 Rover</td>\n",
       "      <td>Through Nov. 1, K-12 students in the U.S. are ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>NASA's Mars Helicopter Attached to Mars 2020 R...</td>\n",
       "      <td>The helicopter will be first aircraft to perfo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>What's Mars Solar Conjunction, and Why Does It...</td>\n",
       "      <td>NASA spacecraft at Mars are going to be on the...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Scientists Explore Outback as Testbed for Mars</td>\n",
       "      <td>Australia provides a great place for NASA's Ma...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>NASA-JPL Names 'Rolling Stones Rock' on Mars</td>\n",
       "      <td>NASA's Mars InSight mission honored one of the...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Robotic Toolkit Added to NASA's Mars 2020 Rover</td>\n",
       "      <td>The bit carousel, which lies at the heart of t...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Space Samples Link NASA's Apollo 11 and Mars 2020</td>\n",
       "      <td>While separated by half a century, NASA's Apol...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Small Satellite Mission of the Year</td>\n",
       "      <td>The first interplanetary CubeSats were recogni...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>NASA 'Optometrists' Verify Mars 2020 Rover's 2...</td>\n",
       "      <td>Mars 2020 rover underwent an eye exam after se...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>New Finds for Mars Rover, Seven Years After La...</td>\n",
       "      <td>NASA's Curiosity rover is discovering odd rock...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>MEDLI2 Installation on Mars 2020 Aeroshell Begins</td>\n",
       "      <td>Hardware installed onto NASA's Mars 2020 entry...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>NASA's Mars 2020 Rover Does Biceps Curls</td>\n",
       "      <td>In this time-lapse video, the robotic arm on N...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>Fueling of NASA's Mars 2020 Rover Power System...</td>\n",
       "      <td>NASA gives the go-ahead to fuel the Mars 2020 ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>What Does a Marsquake Look Like?</td>\n",
       "      <td>InSight scientists used a special \"shake room\"...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>Mars 2020 Rover: T-Minus One Year and Counting</td>\n",
       "      <td>The launch period for NASA's next rover, Mars ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>NASA Racks Up Two Emmy Nominations for Mission...</td>\n",
       "      <td>JPL's coverage of the Mars InSight mission is ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>Want to Colonize Mars? Aerogel Could Help</td>\n",
       "      <td>Researchers are studying whether a wonder mate...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>A Rover Pit Stop at JPL</td>\n",
       "      <td>Working like a finely honed machine, a team of...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>Mars 2020 Rover Gets a Super Instrument</td>\n",
       "      <td>With its rock-zapping laser, the SuperCam will...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>A Neil Armstrong for Mars: Landing the Mars 20...</td>\n",
       "      <td>NASA's newest rover will have an autopilot cal...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>NASA's InSight Uncovers the 'Mole'</td>\n",
       "      <td>The lander's robotic arm has successfully remo...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>Mars 2020 Rover's 7-Foot-Long Robotic Arm Inst...</td>\n",
       "      <td>The main robotic arm has been installed on NAS...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>NASA Selects Partners for Mars 2020 'Name the ...</td>\n",
       "      <td>The contest for U.S. schoolchildren will open ...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                                title  \\\n",
       "0        NASA's Mars 2020 Heads Into the Test Chamber   \n",
       "1   Screening Soon: 'The Pathfinders' Trains Lens ...   \n",
       "2            InSight's 'Mole' Team Peers into the Pit   \n",
       "3             Common Questions about InSight's 'Mole'   \n",
       "4              Mars 2020 Stands on Its Own Six Wheels   \n",
       "5        New Selfie Shows Curiosity, the Mars Chemist   \n",
       "6       Naming a NASA Mars Rover Can Change Your Life   \n",
       "7      Mars 2020 Unwrapped and Ready for More Testing   \n",
       "8   HiRISE Views NASA's InSight and Curiosity on Mars   \n",
       "9   NASA's Curiosity Rover Finds an Ancient Oasis ...   \n",
       "10  NASA's Mars 2020 Rover Tests Descent-Stage Sep...   \n",
       "11  NASA's Push to Save the Mars InSight Lander's ...   \n",
       "12     NASA's InSight 'Hears' Peculiar Sounds on Mars   \n",
       "13  NASA Mars Mission Connects With Bosnian and He...   \n",
       "14  Deadline Closing for Names to Fly on NASA's Ne...   \n",
       "15  NASA Wins Two Emmy Awards for Interactive Miss...   \n",
       "16                 NASA's Mars 2020 Comes Full Circle   \n",
       "17      NASA Invites Students to Name Mars 2020 Rover   \n",
       "18  NASA's Mars Helicopter Attached to Mars 2020 R...   \n",
       "19  What's Mars Solar Conjunction, and Why Does It...   \n",
       "20    Scientists Explore Outback as Testbed for Mars    \n",
       "21       NASA-JPL Names 'Rolling Stones Rock' on Mars   \n",
       "22    Robotic Toolkit Added to NASA's Mars 2020 Rover   \n",
       "23  Space Samples Link NASA's Apollo 11 and Mars 2020   \n",
       "24                Small Satellite Mission of the Year   \n",
       "25  NASA 'Optometrists' Verify Mars 2020 Rover's 2...   \n",
       "26  New Finds for Mars Rover, Seven Years After La...   \n",
       "27  MEDLI2 Installation on Mars 2020 Aeroshell Begins   \n",
       "28          NASA's Mars 2020 Rover Does Biceps Curls    \n",
       "29  Fueling of NASA's Mars 2020 Rover Power System...   \n",
       "30                   What Does a Marsquake Look Like?   \n",
       "31    Mars 2020 Rover: T-Minus One Year and Counting    \n",
       "32  NASA Racks Up Two Emmy Nominations for Mission...   \n",
       "33          Want to Colonize Mars? Aerogel Could Help   \n",
       "34                            A Rover Pit Stop at JPL   \n",
       "35            Mars 2020 Rover Gets a Super Instrument   \n",
       "36  A Neil Armstrong for Mars: Landing the Mars 20...   \n",
       "37                NASA's InSight Uncovers the 'Mole'    \n",
       "38  Mars 2020 Rover's 7-Foot-Long Robotic Arm Inst...   \n",
       "39  NASA Selects Partners for Mars 2020 'Name the ...   \n",
       "\n",
       "                                           title_text  \n",
       "0   In this time-lapse video taken at JPL, enginee...  \n",
       "1   With the Mars 2020 mission ramping up, the doc...  \n",
       "2            Efforts to save the heat probe continue.  \n",
       "3   There's a new plan to get InSight's \"mole\" mov...  \n",
       "4   In time-lapse video, taken at JPL, captures th...  \n",
       "5   The NASA rover performed a special chemistry e...  \n",
       "6   Want to name the robotic scientist NASA is sen...  \n",
       "7   In time-lapse video, bunny-suited engineers re...  \n",
       "8   New images taken from space offer the clearest...  \n",
       "9   New evidence suggests salty, shallow ponds onc...  \n",
       "10  A crane lifts the rocket-powered descent stage...  \n",
       "11  The scoop on the end of the spacecraft's robot...  \n",
       "12  Listen to the marsquakes and other, less-expec...  \n",
       "13  A letter from NASA was presented to the mayor ...  \n",
       "14  You have until Sept. 30 to send your names to ...  \n",
       "15  NASA-JPL's coverage of the Mars InSight landin...  \n",
       "16  Aiming to pinpoint the Martian vehicle's cente...  \n",
       "17  Through Nov. 1, K-12 students in the U.S. are ...  \n",
       "18  The helicopter will be first aircraft to perfo...  \n",
       "19  NASA spacecraft at Mars are going to be on the...  \n",
       "20  Australia provides a great place for NASA's Ma...  \n",
       "21  NASA's Mars InSight mission honored one of the...  \n",
       "22  The bit carousel, which lies at the heart of t...  \n",
       "23  While separated by half a century, NASA's Apol...  \n",
       "24  The first interplanetary CubeSats were recogni...  \n",
       "25  Mars 2020 rover underwent an eye exam after se...  \n",
       "26  NASA's Curiosity rover is discovering odd rock...  \n",
       "27  Hardware installed onto NASA's Mars 2020 entry...  \n",
       "28  In this time-lapse video, the robotic arm on N...  \n",
       "29  NASA gives the go-ahead to fuel the Mars 2020 ...  \n",
       "30  InSight scientists used a special \"shake room\"...  \n",
       "31  The launch period for NASA's next rover, Mars ...  \n",
       "32  JPL's coverage of the Mars InSight mission is ...  \n",
       "33  Researchers are studying whether a wonder mate...  \n",
       "34  Working like a finely honed machine, a team of...  \n",
       "35  With its rock-zapping laser, the SuperCam will...  \n",
       "36  NASA's newest rover will have an autopilot cal...  \n",
       "37  The lander's robotic arm has successfully remo...  \n",
       "38  The main robotic arm has been installed on NAS...  \n",
       "39  The contest for U.S. schoolchildren will open ...  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# my_obj"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "file = my_obj.to_csv('file1.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "## Twitter Handler\n",
    "\n",
    "\n",
    "twitter_browser = webdriver.Chrome('/usr/local/bin/chromedriver 2')\n",
    "\n",
    "## this line asssumes you are already logged in into twitter\n",
    "\n",
    "twitter_browser.get('https://twitter.com/marswxreport?lang=en')\n",
    "\n",
    "\n",
    "web_obj = bs(twitter_browser.page_source,'html.parser')\n",
    "\n",
    "web = web_obj.prettify()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [],
   "source": [
    "web_obj = bs(twitter_browser.page_source,'html.parser')\n",
    "\n",
    "web = web_obj.prettify()\n",
    "\n",
    "# with open('curiosity_page.html','w+') as f:\n",
    "#     f.write(web)\n",
    "    \n",
    "curiosity_tweets = web_obj.find_all('p',{'class':'TweetTextSize'})\n",
    "tweet_list = [e.get_text() for e in curiosity_tweets]\n",
    "\n",
    "tweeted_by = web_obj.find_all('span',{'class':'FullNameGroup'})\n",
    "each_element = [t.get_text() for t in tweeted_by]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# len(curiosity_tweets)==len(tweeted_by)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Property</th>\n",
       "      <th>Value</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Equatorial Diameter:</td>\n",
       "      <td>6,792 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Polar Diameter:</td>\n",
       "      <td>6,752 km</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mass:</td>\n",
       "      <td>6.39 × 10^23 kg (0.11 Earths)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Moons:</td>\n",
       "      <td>2 (Phobos &amp; Deimos)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Orbit Distance:</td>\n",
       "      <td>227,943,824 km (1.38 AU)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Orbit Period:</td>\n",
       "      <td>687 days (1.9 years)</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Surface Temperature:</td>\n",
       "      <td>-87 to -5 °C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>First Record:</td>\n",
       "      <td>2nd millennium BC</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Recorded By:</td>\n",
       "      <td>Egyptian astronomers</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                Property                          Value\n",
       "0   Equatorial Diameter:                       6,792 km\n",
       "1        Polar Diameter:                       6,752 km\n",
       "2                  Mass:  6.39 × 10^23 kg (0.11 Earths)\n",
       "3                 Moons:            2 (Phobos & Deimos)\n",
       "4        Orbit Distance:       227,943,824 km (1.38 AU)\n",
       "5          Orbit Period:           687 days (1.9 years)\n",
       "6  Surface Temperature:                    -87 to -5 °C\n",
       "7          First Record:              2nd millennium BC\n",
       "8           Recorded By:           Egyptian astronomers"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "page = requests.get('https://space-facts.com/mars/')\n",
    "\n",
    "soup_obj=bs(page.text,'html.parser')\n",
    "\n",
    "facts_table = soup_obj.find('table',{'class':'tablepress'})\n",
    "\n",
    "facts_left =facts_table.find_all('td',{'class':'column-1'})\n",
    "facts_right =facts_table.find_all('td',{'class':'column-2'})\n",
    "\n",
    "facts_l_text = [e.get_text() for e in facts_left]\n",
    "facts_r_text = [e.get_text() for e in facts_right]\n",
    "\n",
    "mars_data = {'Property':facts_l_text,\n",
    "             'Value':facts_r_text}\n",
    "\n",
    "structured_data=pd.DataFrame(mars_data)\n",
    "\n",
    "structured_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
