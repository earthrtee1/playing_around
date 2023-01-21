import copy
from collections import deque
import time

start_time = time.time()
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        nodes = {}
        queue = deque()
        visited = set()
        if endWord not in wordList:
            return 0
        x = len(wordList)
        for _ in range(x):
            nodes[wordList[_]] = 0
        queue.append(beginWord)
        if beginWord not in nodes.keys():
            nodes[beginWord] = 0
        
        def findNeighbors(currentNode, nodeDict):
            return_set = set()
            letter_list = list(currentNode)
            x = len(letter_list)
            for _ in range(x):
                disposable_list = copy.deepcopy(letter_list)
                for i in range(97, 123):
                    disposable_list[_] = chr(i)
                    if ''.join(disposable_list) in nodeDict.keys():
                        return_set.add(''.join(disposable_list))
            return return_set

        while queue != deque([]):
            x = queue.pop()
            # print(x)
            visited.add(x)
            # print(visited)
            # print(nodes)
            y = findNeighbors(x, nodes)
            for _ in y:
                if _ not in visited:
                    queue.appendleft(_)
                    if _ == endWord:
                        break
                    elif nodes[_] == 0:
                        nodes[_] = nodes[x] + 1
        # print(nodes)
        # print(nodes[endWord])
        # match beginWord in wordList:
        #     case True:
        #         if nodes[endWord] == 0:
        #             return 0
        #         return nodes[endWord] + 1
        #     case False:
        #         return nodes[endWord]
        if nodes[endWord] == 0:
            return 0
        return nodes[endWord] + 1



x = Solution()
# y = x.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
# y = x.ladderLength("hot", "dog", ["hot","cog","dog","tot","hog","hop","pot","dot"])
y = x.ladderLength("raining", "cellini", ["heaping","conning","nipping","wadding","pulling","lunging","figging","donning","jamming","coating","foaling","ousting","dowsing","busting","penning","lapping","yanking","sapping","tasking","rigging","ranking","larking","farming","dunging","nutting","gouging","barfing","fasting","belting","boiling","boating","dipping","kilning","barking","furling","calving","veiling","decking","ricking","salting","lucking","sending","taiping","marking","martina","warping","bulking","seaming","topping","larding","jilting","besting","weeding","nesting","baiting","jibbing","pelting","bushing","garbing","banting","keeping","venting","rapping","binning","mulling","smiting","hatting","tapping","writing","footing","carding","ratting","bagging","sitting","dousing","pinking","testing","passing","gelling","gassing","ranging","hefting","vamping","wetting","paining","rolling","sinking","yakking","shaking","nabbing","licking","sparing","hamming","celling","halving","matting","landing","kooking","pinning","hagging","narking","soaping","winding","dealing","earring","cunning","moating","skiting","jutting","fueling","hooping","guiling","mapping","hailing","gutting","firming","bunting","mealing","rending","jobbing","pauling","foiling","peeking","rollins","lansing","felling","whiting","vealing","resting","saltine","earning","purging","mullins","pausing","colling","banning","wasting","sealing","gigging","scaring","pocking","massing","curring","storing","dinging","handing","pitting","faining","cupping","staring","riffing","gowning","hipping","vanning","darting","maiming","damping","deaning","bellini","kipling","marting","hawking","fending","kicking","beading","curving","wending","yelling","foaming","rifting","surging","gaining","stoking","panging","winking","nursing","oinking","looking","tolling","bailing","tanking","hacking","warming","cooping","wanting","rotting","kinking","bugging","purling","wincing","joining","belling","wilting","tensing","fellini","wilding","binding","bugling","sagging","nagging","binging","tatting","cellini","silting","belying","ripping","crating","slaking","killing","hurting","running","harming","banding","rinking","staying","touting","hasting","melting","nibbing","talking","ganging","bonging","rilling","damning","pooling","porting","sinning","collins","barbing","bunking","smiling","hanging","tending","bulging","ginning","coiling","lolling","molting","letting","mending","hinging","gunning","melding","dilling","shaving","harping","basting","cobbing","carting","leading","styling","fowling","goading","yowling","zipping","wagging","gaoling","panning","valving","peeling","titling","sailing","harding","parring","haloing","quiting","punting","reeling","batting","signing","pegging","bogging","mashing","rankine","seeding","sassing","wafting","winging","framing","rooting","longing","sabling","bulbing","whiling","balking","canting","dashing","dueling","renting","booting","whaling","vatting","veining","fencing","yucking","slaving","welling","sunning","lulling","purring","dawning","sensing","meaning","wording","hogging","parsing","falling","yelping","dinning","vetting","hulling","reading","lapsing","tooling","hoaxing","roiling","forming","ramming","gelding","felting","popping","walling","costing","welding","washing","filling","lasting","couping","cabling","getting","winning","carping","martins","bilking","burning","jelling","sicking","tinting","ceiling","totting","balding","kenning","tinging","hugging","westing","burring","pasting","pecking","parking","slaying","pigging","heating","manning","bucking","bussing","gagging","goaling","rowling","netting","funking","pitying","jarring","tasting","putting","beating","funding","mauling","balling","molding","shining","perkins","dialing","panting","looping","welting","relying","dulling","dumping","tanning","warring","gatling","staging","finding","farting","petting","picking","swaying","toiling","jambing","bawling","minting","wedding","hulking","keeling","nanking","railing","heading","cutting","gosling","vesting","sighing","mucking","copping","polling","raising","fooling","hooting","titting","calming","seating","rifling","soiling","dubbing","jesting","posting","sacking","corking","yipping","lathing","bopping","setting","coaxing","poshing","fawning","heeling","warning","napping","vending","mooting","hurling","supping","nanjing","pipping","tagging","mopping","souping","palming","gulling","kirking","gilding","docking","wefting","dusting","sharing","darling","bowling","lauding","bidding","hopping","honking","hunting","pepping","busying","damming","patting","hitting","gusting","jigging","gabbing","hosting","sidling","telling","rusting","daubing","reining","memling","healing","gashing","betting","lilting","hashing","salving","firring","gabling","ducking","waiving","skating","worming","waiting","burying","booking","corning","suiting","hooking","gonging","listing","hulaing","sulking","digging","fouling","zincing","cocking","packing","scaling","pooping","zinging","banging","bolling","punning","palling","sipping","bunging","minding","choking","yapping","nicking","warding","gorging","canning","culling","lending","spaying","lashing","pupping","fanning","banking","pinging","roaming","sopping","fonding","searing","fucking","rooking","tooting","raining","billing","pulsing","curbing","cashing","calking","harking","tarring","tacking","whining","tarting","pauline","rasping","howling","helling","curling","pucking","hauling","coaling","lopping","mailing","wailing","lugging","ticking","staving","snaking","selling","masking","jabbing","mewling","heaving","soaring","fagging","cording","begging","ridging","jetting","backing","dotting","lacking","parting","jotting","dunning","tinning","stiling","stating","zapping","hearing","fitting","barging","galling","wigging","feeding","tenting","looting","cabbing","cursing","dunking","dabbing","ragging","bedding","witting","pouting","burping","slating","tamping","basking","failing","papping","narcing","lancing","furlong","tabling","dolling","tailing","pawning","collies","lamming","coifing","bolting","sucking","rafting","morning","ranting","tabbing","rinding","bandung","bashing","bending","ducting","casting","camping","flaming","hinting","sanding","carving","lagging","helping","keening","jolting","temping","junking","manging","dimming","ringing","tipping","spiking","malling","pursing","soaking","willing","fulling","causing","jacking","furring","singing","halting","tucking","ruining","denting","calling","barring","fopping","yawning","tilling","nilling","downing","cooling","martini","budging","lapwing","mincing","rinsing","cowling","marring","coining","sibling","potting","tauting","bulling","lurking","sorting","poohing","bathing","spicing","nailing","spiting","racking","lusting","rutting","gulping","tilting","pairing","peaking","capping","gobbing","finking"])
print("--- %s seconds ---" % (time.time() - start_time))