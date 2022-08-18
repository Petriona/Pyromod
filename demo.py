from pyrogram import enums
data = []
a = []
async for x in bot.search_global(query="this is himanshu rastogi", filter=enums.MessagesFilter.DOCUMENT, limit=100):
 data.append(x)
for x in range(len(data)):
 a.append(dict({'file_size':data[x].document.file_size,'file_id':data[x].document.file_id}))

if not data:
 print('No Files Found')
else:
 try:
  ok = [x['file_id'] for x in a if x['file_size']==max([v['file_size'] for v in a if v['file_size']<1073741824])][0]
  await message.reply_cached_media(ok)
 except:
  ok = [x['file_id'] for x in a if x['file_size']==max([v['file_size'] for v in a if v['file_size']<2147483648])][0]
  await message.reply_cached_media(ok)
