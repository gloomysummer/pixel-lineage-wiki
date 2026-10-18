#!/usr/bin/env python3
"""
Adds Dungeon Exploration Routes and Combat Turn Rotations to each of the 6 race files.
"""

import os

RACE_EXTRA = {
    "nightborn": """
      <!-- Dungeon Exploration & Leveling Route SOP -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Nightborn Exploration & Leveling Route SOP</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          To accelerate your Nightborn character from Level 1 to the Level 30 cap while conserving gold and potions, follow this structured dungeon progression roadmap:
        </p>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399;">Early Game (Levels 1–10): Sunken Crypts & Goblin Caverns</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Exploit your +15% passive MP regeneration to cast spells on every single combat turn without drinking mana potions. Conserving early gold allows you to purchase Tier-1 Iron Gear from the Blacksmith immediately upon hitting Level 10.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8;">Mid Game (Levels 11–20): Act 2 The Dungeon & Trainer's Shrine</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Locate the Trainer's Shrine in Act 2 to awaken into Hexer or Cleric. With Nightborn's +8% Dark Spell amplifier active, cast Shadow Decay curses on entire monster rooms: the multi-target damage ticks wipe waves while refilling your mana pool automatically.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #a855f7;">
            <strong style="color: #a855f7;">End Game (Levels 21–30): Torment Chambers & Guild Raids</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Equip Shadowsilk Vestments and the Bloodstone Amulet. Stack critical strike chance to trigger continuous 20%+ lifesteal. In 4-player Guild Raids, your infinite mana sustain ensures you can maintain continuous offensive curses without taxing the party healer.
            </p>
          </div>
        </div>
      </section>

      <!-- Multiplayer Combat Turn Rotation Blueprint -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Tactical Turn-by-Turn Combat Rotation Blueprint</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Maximize your party damage output and personal survival by executing this battle rotation during tough boss encounters:
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #a855f7; display: block; margin-bottom: 4px;">Turn 1: Opener & Shielding</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Cast Mana Barrier (1 EP) to establish initial physical shielding, followed by Shadow Curse on the boss to initiate multi-turn decay scaling.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #34d399; display: block; margin-bottom: 4px;">Turn 2: Burst & Lifesteal Proc</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Unleash Void Volley. Each projectile has an independent critical roll; landing crits triggers Nightborn's 15% lifesteal, completely replenishing any chipped shield HP.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #f43f5e; display: block; margin-bottom: 4px;">Turn 3: Finisher or Cleanse</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              With 3 accumulated Energy Points, detonate Nether Cataclysm for massive burst damage, or cycle Mana Barrier if the boss initiates an enrage attack cycle.
            </p>
          </div>
        </div>
      </section>
""",
    "celestine": """
      <!-- Dungeon Exploration & Leveling Route SOP -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Celestine Exploration & Leveling Route SOP</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Celestine excels as the team anchor. Follow this leveling progression to transition smoothly from solo novice to the premier raid cleanser:
        </p>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399;">Early Game (Levels 1–10): Sunken Ruins Solo Expeditions</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Target Undead-type bats and skeletons in the Sunken Ruins. Celestine's +12% Holy spell damage tears through undead mobs, letting you clear rooms swiftly while taking minimal counter-attack damage.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8;">Mid Game (Levels 11–20): Act 2 Crypts & Cleric Awakening</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Awaken as a Cleric or Paladin Sentinel. In the poisonous Crypt corridors, Celestine's innate 25% turn start cleanse eliminates virulent poison stacks, keeping party health bars pristine.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #c9a227;">
            <strong style="color: #c9a227;">End Game (Levels 21–30): Torment Colossus & Abyss Raids</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Equip Blessed Templar Vestments. In Torment Mode, boss debuffs like Miasma and Curse are lethal wipe conditions. Celestine's dual cleanse aura ensures your party survives extended 10+ turn attrition wars.
            </p>
          </div>
        </div>
      </section>

      <!-- Multiplayer Combat Turn Rotation Blueprint -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Tactical Turn-by-Turn Combat Rotation Blueprint</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Coordinate with your party by following this standard support and purification rotation:
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #38bdf8; display: block; margin-bottom: 4px;">Turn 1: Divine Aegis & Ward</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Cast Divine Ward on your frontline tank to apply +8% magical damage reduction, buffering them against the boss's opening elemental strike.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #34d399; display: block; margin-bottom: 4px;">Turn 2: Cleanse Roll & Group Prayer</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Turn start automatically rolls for a debuff cleanse. Follow up with Holy Radiance to heal all injured teammates for 350+ HP with Aura of Grace amplification.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #c9a227; display: block; margin-bottom: 4px;">Turn 3: Holy Smite Vulnerability</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Unleash Holy Smite on the boss. This applies a secondary vulnerability debuff, granting all teammate physical attacks +10% true damage for 2 rounds.
            </p>
          </div>
        </div>
      </section>
""",
    "seraph": """
      <!-- Dungeon Exploration & Leveling Route SOP -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Seraph Exploration & Leveling Route SOP</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Seraph dominates speed progression. Follow this leveling blueprint to leverage your aerial agility and true damage:
        </p>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399;">Early Game (Levels 1–10): Rapid Clearing & Double-Turn Kiting</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Seraph's +10% Speed allows you to take two actions before basic forest goblins act once. Use rapid archery or dagger strikes to wipe mobs before they close into melee range.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8;">Mid Game (Levels 11–20): Featherfall Maze Traversal</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              In Act 2 The Dungeon, treacherous floor spikes and falling rubble traps deal heavy damage to grounded characters. Featherfall ignores all floor hazard triggers, allowing you to bypass traps without pausing.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #c9a227;">
            <strong style="color: #c9a227;">End Game (Levels 21–30): Armor-Piercing Raid Finisher</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Equip Windwalker Leathers and Zephyr Longbow. Torment bosses feature extreme physical armor values (over 70% DR). Seraph's 8% True Damage on hit bypasses this armor completely, dealing consistent DPS throughout enrage phases.
            </p>
          </div>
        </div>
      </section>

      <!-- Multiplayer Combat Turn Rotation Blueprint -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Tactical Turn-by-Turn Combat Rotation Blueprint</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Execute this high-tempo rotation to maximize true damage application while evading retaliation:
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #c9a227; display: block; margin-bottom: 4px;">Turn 1: Turn Priority & Evasion Dash</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Act first via superior Speed. Activate Zephyr Dash (+20% Evasion for 2 rounds) and apply Hunter's Mark to enhance target vulnerability.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #38bdf8; display: block; margin-bottom: 4px;">Turn 2: Multi-Hit True Damage Barrage</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Unleash 5-Arrow Flurry. Each arrow hit procs Seraph's 8% True Damage independently, bypassing boss defense five times in one turn.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #f43f5e; display: block; margin-bottom: 4px;">Turn 3: Aerial Reposition & Snipe</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Take second action before boss recovery. Execute Archon Snipe from maximum distance, finishing off high-threat adds or staggering the boss gauge.
            </p>
          </div>
        </div>
      </section>
""",
    "dullahan": """
      <!-- Dungeon Exploration & Leveling Route SOP -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Dullahan Exploration & Leveling Route SOP</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Dullahan is the unstoppable frontline juggernaut. Follow this leveling progression to build an unkillable raid vanguard:
        </p>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399;">Early Game (Levels 1–10): Heavy Armor Mastery & Unbreakable Poise</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Equip the heaviest plate armor available. Dullahan's +18% armor multiplier boosts early Iron sets into impenetrable armor, while Headless Poise nullifies goblin stuns completely.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8;">Mid Game (Levels 11–20): Act 2 Dungeon Vanguard Tanking</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Awaken into Sentinel or Greatsword Warrior. Face-tank skeletal hordes and boss charging attacks without suffering stagger delays, allowing your backline spellcasters to channel freely.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #f43f5e;">
            <strong style="color: #f43f5e;">End Game (Levels 21–30): Raid Aggro & 15% Decapitate Execution</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Equip Juggernaut Bulwark Plate. In Torment Raids, bosses gain deadly enrage buffs below 20% HP. Dullahan's Decapitation Strike executes the boss at 15% health, skipping the wipe phase entirely.
            </p>
          </div>
        </div>
      </section>

      <!-- Multiplayer Combat Turn Rotation Blueprint -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Tactical Turn-by-Turn Combat Rotation Blueprint</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Hold frontline threat and execute wounded targets by executing this rotation:
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #f43f5e; display: block; margin-bottom: 4px;">Turn 1: Roar of the Headless Rider</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Activate War Taunt to lock boss targeting onto your character, while gaining +15% block chance for the next 2 rounds.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #38bdf8; display: block; margin-bottom: 4px;">Turn 2: Unyielding Bulwark Stance</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Fortify defensive stance. Physical damage mitigation hits over 72%, easily absorbing incoming unblocked boss cleaves.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #c9a227; display: block; margin-bottom: 4px;">Turn 3: Decapitate Strike Finisher</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              When the boss's HP drops to 15% or below, trigger Decapitate Strike to deal instantaneous fatal damage, ending the encounter immediately.
            </p>
          </div>
        </div>
      </section>
""",
    "orc": """
      <!-- Dungeon Exploration & Leveling Route SOP -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Orc Exploration & Leveling Route SOP</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Orc is built for aggressive damage trading. Follow this leveling path to maximize your raw health and berserk power spikes:
        </p>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399;">Early Game (Levels 1–10): Aggressive Trading in Act 1 Caverns</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Orc's +12% base HP pool provides a massive health buffer. Trade hits fearlessly against early monsters, allowing low-HP rage to trigger for fast wave clears without needing early armor upgrades.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8;">Mid Game (Levels 11–20): Berserk & Brawler Evolution</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Awaken as a Berserker Warrior or Fist Brawler. In Act 2 The Dungeon, master health balancing: keep your health hovering around 25–30% to maintain constant +15% bonus attack scaling.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #ea580c;">
            <strong style="color: #ea580c;">End Game (Levels 21–30): True Damage Absorption in Torment</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Equip Warlord Heavy Plate and Bloodstone Totem. Act 3 Colossus bosses deal true damage that ignores all physical defense; an Orc's 650+ unmitigated HP pool is the only setup capable of surviving multiple direct slams.
            </p>
          </div>
        </div>
      </section>

      <!-- Multiplayer Combat Turn Rotation Blueprint -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Tactical Turn-by-Turn Combat Rotation Blueprint</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Maximize your enraged damage output and health recovery cycles by executing this combat rotation:
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #ea580c; display: block; margin-bottom: 4px;">Turn 1: Battle Cry & Aggro Lock</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Unleash Battle Cry to draw monster aggro onto your 650+ HP buffer, reducing party incoming damage by 15% for 2 rounds.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #f43f5e; display: block; margin-bottom: 4px;">Turn 2: Enraged Counter-Cleave</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              As boss attacks push you below 30% HP, Berserk Rage triggers (+15% ATK). Strike with Bloodthirst Cleave, dealing boosted damage and restoring 12% health.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #34d399; display: block; margin-bottom: 4px;">Turn 3: Iron Stun Slam</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Execute heavy ground slam. High base attack combined with rage bonus inflicts a 25% Action Gauge delay on the boss, resetting your survival window.
            </p>
          </div>
        </div>
      </section>
""",
    "elf": """
      <!-- Dungeon Exploration & Leveling Route SOP -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #fff; margin: 0 0 16px;">Elf Exploration & Leveling Route SOP</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Elf is the ultimate long-range precision lineage. Follow this leveling guide to maintain safe engagement distances and high critical uptime:
        </p>

        <div style="display: flex; flex-direction: column; gap: 14px;">
          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #34d399;">
            <strong style="color: #34d399;">Early Game (Levels 1–10): Safe Distance Sniping</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Elf's +10% base Critical Strike Chance means nearly a quarter of your early shots deal double damage. Keep maximum grid distance to eliminate Act 1 goblins before they close within melee reach.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #38bdf8;">
            <strong style="color: #38bdf8;">Mid Game (Levels 11–20): Sniper & Assassin Awakening</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Awaken as a Sniper Archer or Shadow Assassin. In Act 2 The Dungeon, use +12% projectile velocity to bypass frontline summons and eliminate rear necromancers directly.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px 16px; border-radius: 6px; border-left: 3px solid #22c55e;">
            <strong style="color: #22c55e;">End Game (Levels 21–30): High-Evasion Torment Kiting</strong>
            <p style="color: var(--muted); font-size: 0.88rem; line-height: 1.5; margin: 4px 0 0;">
              Equip Sylph Shadowgarb and Ancient Elven Greatbow. Stacking Forest Stride with gear pushes evasion past 25%, while critical strike rates exceed 40%, shredding Torment raid bosses from safety.
            </p>
          </div>
        </div>
      </section>

      <!-- Multiplayer Combat Turn Rotation Blueprint -->
      <section style="background: #161022; border: 1px solid var(--line); border-radius: 8px; padding: 24px; margin-bottom: 36px;">
        <h2 style="font-size: 1.3rem; color: #c9a227; margin: 0 0 16px;">Tactical Turn-by-Turn Combat Rotation Blueprint</h2>
        <p style="color: var(--muted); font-size: 0.95rem; line-height: 1.6; margin: 0 0 16px;">
          Execute this precision rotation to maximize critical damage while maintaining defensive evasion:
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #22c55e; display: block; margin-bottom: 4px;">Turn 1: Hunter's Precision Mark</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Cast Precision Mark from maximum range, increasing boss critical vulnerability by 10% for the entire party.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #f43f5e; display: block; margin-bottom: 4px;">Turn 2: High-Velocity Piercing Snipe</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Unleash Piercing Arrow. With over 40% crit chance and 1.8x multiplier, this strike deals massive burst damage that bypasses enemy armor.
            </p>
          </div>

          <div style="background: #0d0a14; padding: 14px; border-radius: 6px; border: 1px solid var(--line);">
            <strong style="color: #38bdf8; display: block; margin-bottom: 4px;">Turn 3: Forest Stride Tactical Evasion</strong>
            <p style="color: var(--muted); font-size: 0.85rem; line-height: 1.5; margin: 0;">
              Trigger Forest Stride to reposition back 2 grid tiles, raising evasion to 35% against any incoming enemy ranged retaliation.
            </p>
          </div>
        </div>
      </section>
"""
}

for race_key, extra_content in RACE_EXTRA.items():
    path = f"src/pages/races/{race_key}.astro"
    if not os.path.exists(path):
        print(f"File not found: {path}")
        continue
    
    content = open(path).read()
    if "Exploration & Leveling Route SOP" in content:
        print(f"{race_key} already has routes, skipping.")
        continue
    
    # Marker: Before <!-- Reroll Strategy --> or <!-- Spin Economics --> or <!-- Event Availability & Reroll Warning -->
    markers = [
        "<!-- Reroll Strategy -->",
        "<!-- Spin Economics -->",
        "<!-- Event Availability & Reroll Warning -->"
    ]
    
    found = False
    for m in markers:
        if m in content:
            content = content.replace(m, extra_content + "\n      " + m, 1)
            found = True
            break
            
    if found:
        with open(path, "w") as f:
            f.write(content)
        print(f"Successfully added routes and rotations to {race_key}")
    else:
        print(f"Could not find marker in {race_key}")

print("Route injection complete.")
