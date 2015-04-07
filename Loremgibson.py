import sublime
import sublime_plugin
import random


class LoremgibsonCommand(sublime_plugin.TextCommand):


    @classmethod
    def generate_sentence(self, length=5):
        basetext = ['concrete', 'face forwards', 'hotdog', 'futurity', 'motion', 'bridge', 'drugs', 'realism', 'dome', 'sign', 'A.I.', 'warehouse', 'bomb', 'receding', 'fluidity', 'franchise', 'towards', 'neon', 'rifle', 'kanji', 'saturation point', 'ablative', 'skyscraper', 'car', 'pen', 'soul-delay', 'tower', '-space', '-ware', 'digital', 'wristwatch', 'advert', 'boat', 'jeans', 'physical', 'DIY', 'sentient', 'render-farm', 'city', 'corporation', 'table', 'free-market', 'Chiba', 'smart-', 'Shibuya', 'silent', 'numinous', 'semiotics', 'girl', 'assault', 'drone', 'refrigerator', 'euro-pop', 'savant', 'uplink', 'j-pop', 'grenade', 'computer', 'youtube', 'knife', 'artisanal', 'RAF', 'rebar', 'apophenia', 'tube', 'sensory', 'San Francisco', 'garage', 'market', 'vinyl', 'cartel', 'meta-', 'katana', 'rain', 'corrupted', 'range-rover', 'hacker', 'narrative', 'shanty town', 'Legba', 'faded', 'systema', 'nano-', 'bicycle', 'nodal point', 'monofilament', 'order-flow', 'footage', 'long-chain hydrocarbons', 'papier-mache', 'nodality', 'crypto-', 'engine', 'stimulate', 'lights', 'carbon', 'singularity', 'modem', 'denim', 'math-', 'plastic', 'fetishism', 'urban', 'sub-orbital', 'dead', 'Kowloon', 'paranoid', 'sunglasses', 'voodoo god', 'pre-', 'pistol', 'gang', '3D-printed', 'courier', 'construct', 'vehicle', 'sprawl', 'marketing', 'augmented reality', 'Tokyo', 'tanto', 'dolphin', 'chrome', 'office', 'neural', '8-bit', 'film', 'shrine', 'network', 'beef noodles', 'post-', 'woman', 'military-grade', 'tattoo', 'into', 'cyber-', 'man', 'disposable', 'spook', 'wonton soup', 'tiger-team', 'decay', 'weathered', 'tank-traps', 'media', 'assassin', 'industrial grade', 'systemic', 'BASE jump', 'convenience store', 'camera', 'cardboard', 'alcohol', 'claymore mine', 'shoes', 'boy', 'otaku', 'human', 'geodesic', 'dissident']
        random.shuffle(basetext)
        sentence = basetext[0:length]
        sentence[0] = sentence[0][0].upper() + sentence[0][1:]  # upcase first char of sentence
        sentence[-1] = sentence[-1] + '.'  # adding some punctuation
        sentence = ' '.join(sentence)
        return sentence

    @classmethod
    def generate_paragraph(self, length=4):
        paragraph = []
        for i in range(length):
            paragraph.append(LoremgibsonCommand.generate_sentence(random.randint(7, 17)))
        return ' '.join(paragraph)


    def run(self, edit):
        out = LoremgibsonCommand.generate_paragraph(random.randint(3, 9))
        out = out.replace('- ', '-')
        out = out.replace(' -', '-')
        out = out.replace('-.', '.')
        out = out + ' '
        self.view.insert(edit, self.view.sel()[0].begin(), out)
