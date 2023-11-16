from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image
from io import BytesIO
import base64

driver = webdriver.Edge()

def get_blob_image(uri):
  result = driver.execute_async_script("""
    var uri = arguments[0];
    var callback = arguments[1];
    var toBase64 = function(buffer){for(var r,n=new Uint8Array(buffer),t=n.length,a=new Uint8Array(4*Math.ceil(t/3)),i=new Uint8Array(64),o=0,c=0;64>c;++c)i[c]="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charCodeAt(c);for(c=0;t-t%3>c;c+=3,o+=4)r=n[c]<<16|n[c+1]<<8|n[c+2],a[o]=i[r>>18],a[o+1]=i[r>>12&63],a[o+2]=i[r>>6&63],a[o+3]=i[63&r];return t%3===1?(r=n[t-1],a[o]=i[r>>2],a[o+1]=i[r<<4&63],a[o+2]=61,a[o+3]=61):t%3===2&&(r=(n[t-2]<<8)+n[t-1],a[o]=i[r>>10],a[o+1]=i[r>>4&63],a[o+2]=i[r<<2&63],a[o+3]=61),new TextDecoder("ascii").decode(a)};
    var xhr = new XMLHttpRequest();
    xhr.responseType = 'arraybuffer';
    xhr.onload = function(){ callback(toBase64(xhr.response)) };
    xhr.onerror = function(){ callback(xhr.status) };
    xhr.open('GET', uri);
    xhr.send();
    """, uri)
  if type(result) == int :
    raise Exception("Request failed with status %s" % result)
  return Image.open(BytesIO(base64.b64decode(result)))

driver.get("https://clipdrop.co/stable-diffusion")

yes = input("did u sign in y/n")
search = driver.find_element(by=By.NAME,value="input-prompt")

search.send_keys("It’s the end of the year- there is an annual performance and the girls in the . 4th are super active and enthusiastic. Rember that it take place in indian.school. The theme of the image should be upbright .")

element = driver.find_element(By.XPATH, "//*[contains(text(), 'Generate')]")
element.click()

time.sleep(100)

imgs = driver.find_elements(By.XPATH , "//img[@class='w-full h-full rounded-xl object-contain']")

print(imgs)

for img_obj in imgs:
    img_src = img_obj.get_attribute("src")
    image = get_blob_image(img_src)
    image.save('hei2.jpg','JPEG')


driver.close()
