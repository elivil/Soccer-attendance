from bs4 import BeautifulSoup

html = """<td width="23%" style="text-align:right;vertical-align:top" class="vcard attendee"><b><span class="fn org">AS Monaco</span></b>
</td>
<td width="12%" style="text-align:center;vertical-align:top"><span style="white-space:nowrap; display:inline;"><b>3–2</b></span>
</td>
<td width="23%" style="vertical-align:top" class="vcard attendee"><b><span class="fn org"><a href="/wiki/Toulouse_FC" title="Toulouse FC">Toulouse</a></span></b>
</td>"""

soup = BeautifulSoup(html, 'html.parser')

print(soup.td.span.contents[0].string)
