"""_summary_

    Using crazytext library

"""
import crazytext as ct_lib

# ----------------------------------------------------
# Clean Text Data in one Line with crazytext - Cleaner
# ----------------------------------------------------

TEXT_EXAMPLE = '''
    <p>Superman</p> (@supermafromsky) <b>Belongs to SKY ID</b> superman@sky.com #superman #batman #justiceleague
    AI is the future of HUMAN KIND, & Trendiest Topic of Today.
    #ai #future @aiforfuture https://ai.com  (555) 555-1234
    # <p> Mobile Number </p> (555) 345-1234  <span>Pincode:</span> 224 '
'''

cleaner = ct_lib.Cleaner(text=TEXT_EXAMPLE)
print(cleaner.quick_clean(remove_complete=False, make_base=False))

print(" ")
# ----------------------------------------------------
# Clean Text Data in one Line with crazytext - Counter
# ----------------------------------------------------
print(" ")

result_counter = ct_lib.Counter(text=TEXT_EXAMPLE)
print(result_counter.info())

print(" ")
# ----------------------------------------------------
# Clean Text Data in one Line with crazytext - Extractor
# ----------------------------------------------------
print(" ")

result_extractor = ct_lib.Extractor(text=TEXT_EXAMPLE)
print(result_extractor.info())
print(result_extractor.get_emails())
print(result_extractor.get_hashtags())
print(result_extractor.get_mentions())
print(result_extractor.get_urls())
print(result_extractor.get_phone_numbers())
print(result_extractor.get_uppercase_words())
print(result_extractor.get_html_tags())
