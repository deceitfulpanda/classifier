#!/usr/bin/env python

import flickrapi, unirest, time

api_key = u'bd357bbf22b783cd194d9585e495e0a4'
api_secret = u'8be92d6e6304428a'

flickr = flickrapi.FlickrAPI(api_key, api_secret)

def open_file(filename):
  # read file line by line into a list
  with open(filename) as f:
    items = f.readlines()

  # remove newline characters from list items
  items = [x.strip('\n') for x in items]

  for item in items:
    print item
    # search for query
    search_flickr(item)

def search_flickr(query):
  # grab photo urls from flickr
  photos = flickr.photos.search(text=query, sort='relevance')

  photo_urls = []

  # parse photo data
  for i in range(0, 2):
    attributes = photos[0][i].attrib
    photo_urls.append('https://farm' + attributes['farm'] +
      '.staticflickr.com/' + attributes['server'] + '/' +
      attributes['id'] + '_' + attributes['secret'] + '_m.jpg')

  for url in photo_urls:
    read_image(url)

def read_image(photo_url):
  post_res = unirest.post("https://camfind.p.mashape.com/image_requests",
    headers = {
      "X-Mashape-Key": "EPlpijnycCmshxK3kiQgglPopllsp1WWLaijsntHB14joITe8x",
      "Content-Type": "application/x-www-form-urlencoded",
      "Accept": "application/json"
    },
    params = {
      "image_request[locale]": "en_US",
      "image_request[remote_image_url]": photo_url
    }
  )
  
  return get_description(post_res.body['token'])

def check_res(token):
  time.sleep(20)
  
  response = unirest.get("https://camfind.p.mashape.com/image_responses/" + token,
    headers = {
      "X-Mashape-Key": "EPlpijnycCmshxK3kiQgglPopllsp1WWLaijsntHB14joITe8x",
      "Accept": "application/json"
    }
  )
 
  return response

def get_description(token):
  time.sleep(20)
  
  description = unirest.get("https://camfind.p.mashape.com/image_responses/" + token,
    headers = {
      "X-Mashape-Key": "EPlpijnycCmshxK3kiQgglPopllsp1WWLaijsntHB14joITe8x",
      "Accept": "application/json"
    }
  )

  description = check_res(token)

  if not description.body.has_key('name'):
    description = check_res(token)

  print description.body

  if description.body.has_key('reason'):
    return 'skipped'
  else:
    return save_description(description.body['name'])

def save_description(desc):
  with open('landfill-desc.txt', 'a') as f:
    f.write(desc + '\n')

# COMPLETED
# aluminum can
# aluminum foil
# aluminum tray
# bottle cap
# steel can lid
# tin can lid
# jar lid
# paint can
# spray can
# steel can
# tin can
# plastic bottle
# plastic bucket
# CD
# DVD
# CDROM
# CD case
# DVD case
# CDROM case
# coffee cup lid
# plastic container
# clamshell
# plastic cork
# plastic cup
# plastic plates
# plastic flower pot
# plastic tray
# laundry detergent bottle
# molded plastic packaging
# toy
# plastic tub
# plastic lid
# yogurt container
# tupperware
# plastic utensil
# plastic bag
# cardboard
# cereal box
# paperboard
# computer paper
# office paper
# egg carton
# envelope
# mail
# magazine
# newspaper
# packing paper
# kraft paper
# phonebook
# sticky note
# shredded paper
# wrapping paper
# glass bottle
# glass jar
# metal cap
# metal lid
#
# bread
# grains
# pasta
# coffee grounds
# coffee filter
# dairy
# eggshells
# eggs
# fruit
# fruit pits
# fruit shells
# leftovers
# spoiled food
# meat
# meat bones
# seafood
# shellfish
# tea
# vegetable
# pizza box
# paper cup
# paper plate
# paper ice cream container
# paper napkin
# paper tissue
# paper towel
# paper take-out box
# tissues
# milk carton
# juice carton
# branches
# brush
# flowers
# floral trimmings
# grasses
# weeds
# leaves
# tree trimmings
# cotton balls
# cotton swabs
# hair
# fur
# feathers
# vegetable wood crates
# waxed cardboard
# waxed paper
# wood
# wooden chopsticks

# TO DO
# plastic-backed paper
# glass mirror
# glass window
# incandescent light bulb
# juice foil liner box
# soy milk foil liner box
# mylar bag
# potato chip bag
# candy bar wrapper
# balloon
# pen
# pencil
# plastic bag
# plastic wrapper
# plastic film
# biodegradable plastic
# metal
# fabric
# rubber
# rubber bands
# six-pack ring holder
# sponge
# styrofoam
# twwist tie
# plywood
# pressboard
# painted wood
# stained wood