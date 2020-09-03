#----------------------------------------------------------------------------
# Program by Cherkasov.R.
#
#
# Version   Date        Info
# 0.1       03.09.20    Copying svg-tag from SVG file to VUE file.
#----------------------------------------------------------------------------


""""Adding by full path, checking file type (in progress) """
# path = str(input())
# if path.rfind('.svg') == -1:
#     print("Wrong file, please use svg-file")

from bs4 import BeautifulSoup

with open("cart.svg", "r") as f:
    contents = f.read()

    soup = BeautifulSoup(contents, 'lxml')

    print(soup.svg)

outputFile = open('outputFile.vue', 'tw', encoding='utf-8')
text_start = "<template>\n"
text_end ="""</template>

<script>
export default {
  name: 'name'
}
</script>

<style scoped lang="scss"></style>"""
outputFile.write(text_start + str(soup.svg) +"\n" + text_end )

outputFile.close()
    #print(soup.head)
   #print(soup.li)