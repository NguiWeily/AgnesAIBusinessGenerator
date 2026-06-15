const BusinessPlanTool = (() => {
  const normalize = text => text.trim().toLowerCase();

  const chooseModel = description => {
    const text = normalize(description);
    if (/(saas|software|app|platform)/.test(text)) return 'SaaS / Software';
    if (/(course|coaching|training|education|tutoring)/.test(text)) return 'Digital education / coaching';
    if (/(e-commerce|store|shop|product|retail)/.test(text)) return 'E-commerce / online store';
    if (/(consulting|agency|freelance|service)/.test(text)) return 'Service business / consulting';
    if (/(subscription|membership|community)/.test(text)) return 'Subscription / membership';
    if (/(content|blog|youtube|podcast)/.test(text)) return 'Content creation / creator business';
    return 'Home-based small business';
  };

  const chooseTarget = description => {
    const text = normalize(description);
    if (text.includes('small business') || text.includes('startup')) return 'Small business owners and founders looking for practical solutions.';
    if (text.includes('family') || text.includes('parent') || text.includes('kids')) return 'Busy families and parents who need convenient solutions.';
    if (text.includes('student') || text.includes('students')) return 'Students and lifelong learners seeking practical skills.';
    if (text.includes('pet') || text.includes('animal')) return 'Pet owners who want better care and convenience.';
    if (text.includes('health') || text.includes('wellness') || text.includes('fitness')) return 'Health-conscious individuals who want lifestyle improvement.';
    return 'Local and online customers who want a simple, high-value solution from a trusted home business.';
  };

  const chooseValueProposition = description => `Create a low-overhead home business offering ${description}. Focus on fast delivery, clear pricing, and an easy digital presence.`;

  const estimateRevenue = description => {
    const model = chooseModel(description);
    switch (model) {
      case 'SaaS / Software':
        return ['Monthly subscriptions', 'Annual licenses', 'Premium support plans', 'Add-on features'];
      case 'Digital education / coaching':
        return ['Course sales', 'Coaching packages', 'Group workshops', 'Digital downloads'];
      case 'E-commerce / online store':
        return ['Product sales', 'Bundles', 'Repeat purchases', 'Cross-sell accessories'];
      case 'Service business / consulting':
        return ['Project fees', 'Hourly retainers', 'Recurring contracts', 'Referral bonuses'];
      case 'Subscription / membership':
        return ['Monthly memberships', 'Premium tiers', 'Community access', 'Add-on services'];
      case 'Content creation / creator business':
        return ['Ad revenue', 'Sponsorships', 'Affiliate sales', 'Paid content'];
      default:
        return ['Direct clients', 'Small product sales', 'Online offers', 'Referral income'];
    }
  };

  const estimateBudget = description => {
    const model = chooseModel(description);
    if (model === 'SaaS / Software') {
      return {
        'Website and hosting': '$300 - $1,200',
        'Domain and SSL': '$20 - $80',
        'Development tools': '$0 - $500',
        'Marketing / launch': '$500 - $2,000',
        'Legal / business setup': '$200 - $800',
      };
    }
    if (model === 'Digital education / coaching') {
      return {
        'Course platform / LMS': '$100 - $500',
        'Video / audio equipment': '$200 - $1,000',
        'Marketing / ads': '$300 - $1,500',
        'Website / landing page': '$100 - $400',
        'Legal / contracts': '$100 - $500',
      };
    }
    if (model === 'E-commerce / online store') {
      return {
        'Inventory / samples': '$500 - $3,000',
        'Shop setup': '$100 - $400',
        'Packaging / shipping': '$200 - $800',
        'Marketing / social ads': '$400 - $1,500',
        'Business registration': '$100 - $300',
      };
    }
    if (model === 'Service business / consulting') {
      return {
        'Website / professional profile': '$100 - $300',
        'Tools / software': '$50 - $300',
        'Marketing / networking': '$200 - $800',
        'Professional insurance': '$150 - $500',
        'Business license': '$50 - $250',
      };
    }
    if (model === 'Subscription / membership') {
      return {
        'Community platform': '$150 - $600',
        'Content creation': '$200 - $800',
        'Marketing': '$300 - $1,200',
        'Support systems': '$100 - $400',
        'Legal / terms': '$150 - $500',
      };
    }
    return {
      'Basic website': '$100 - $300',
      'Home office setup': '$100 - $500',
      'Marketing': '$200 - $800',
      'Software tools': '$50 - $300',
      'Legal / registration': '$100 - $400',
    };
  };

  const estimateCashflow = description => {
    const model = chooseModel(description);
    if (model === 'SaaS / Software') {
      return {
        'Month 1-3': 'Build an MVP, start outreach, and validate product-market fit.',
        'Month 4-6': 'Acquire early customers, improve onboarding, and refine pricing.',
        'Month 7-12': 'Scale marketing, improve retention, and target a recurring base.',
      };
    }
    if (model === 'Digital education / coaching') {
      return {
        'Month 1-3': 'Create the core program, pre-launch to an audience, and gather initial signups.',
        'Month 4-6': 'Launch publicly, collect testimonials, and expand paid traffic.',
        'Month 7-12': 'Optimize sales funnels, increase upsells, and retain clients.',
      };
    }
    if (model === 'E-commerce / online store') {
      return {
        'Month 1-3': 'Source inventory, launch the store, and test initial ads.',
        'Month 4-6': 'Refine product mix, improve margins, and increase repeat orders.',
        'Month 7-12': 'Expand offerings, optimize logistics, and scale customer acquisition.',
      };
    }
    if (model === 'Service business / consulting') {
      return {
        'Month 1-3': 'Define service packages, land initial clients, and refine pricing.',
        'Month 4-6': 'Secure recurring contracts and collect referrals.',
        'Month 7-12': 'Build predictable revenue and systemize delivery.',
      };
    }
    if (model === 'Subscription / membership') {
      return {
        'Month 1-3': 'Validate the concept, recruit founding members, and test the offering.',
        'Month 4-6': 'Grow membership and add premium benefits.',
        'Month 7-12': 'Improve retention and increase average revenue per member.',
      };
    }
    return {
      'Month 1-3': 'Validate the idea, set up the business, and secure first customers.',
      'Month 4-6': 'Grow awareness, build repeat business, and manage costs.',
      'Month 7-12': 'Move to positive cashflow and invest in growth.',
    };
  };

  const estimateLicenses = description => {
    const text = normalize(description);
    const licenses = ['General business license / local registration'];
    if (/(food|cafe|restaurant|catering)/.test(text)) licenses.push('Health department permit');
    if (/(child|kids|education|tutor)/.test(text)) licenses.push('Home child care / education permit if needed');
    if (/(construction|electrician|plumbing|contractor)/.test(text)) licenses.push('Trade or professional license');
    if (/(retail|shop|store)/.test(text)) licenses.push('Sales tax permit');
    if (/(professional|consulting|therapy)/.test(text)) licenses.push('Professional liability insurance and contracts');
    if (/(online|digital)/.test(text)) licenses.push('E-commerce compliance and privacy policy');
    return licenses;
  };

  const estimateSkills = description => {
    const skills = ['Customer research', 'Basic bookkeeping', 'Online marketing', 'Project planning'];
    const text = normalize(description);
    if (/(website|e-commerce|online|digital)/.test(text)) skills.push('Web presence and digital marketing');
    if (/(course|coaching|training)/.test(text)) skills.push('Instructional design and client coaching');
    if (/(consult|service|agency)/.test(text)) skills.push('Client communication and sales');
    if (/(product|manufacturing|shop)/.test(text)) skills.push('Product sourcing and supply chain');
    if (/(saas|software|app)/.test(text)) skills.push('Product development and user experience');
    return [...new Set(skills)];
  };

  const timelineFirstMillion = description => {
    const model = chooseModel(description);
    switch (model) {
      case 'SaaS / Software':
        return '18-30 months with aggressive user acquisition and recurring revenue.';
      case 'Digital education / coaching':
        return '12-24 months if you build a flagship high-ticket offer and scale with digital funnels.';
      case 'E-commerce / online store':
        return '24-36 months depending on margins and repeat purchases.';
      case 'Service business / consulting':
        return '24-48 months if you convert high-value clients and scale retention.';
      case 'Subscription / membership':
        return '18-30 months with strong retention and membership growth.';
      default:
        return '24-42 months for a home business starting from scratch and reinvesting profits.';
    }
  };

  const buildPlan = description => {
    const model = chooseModel(description);
    const plan = {
      description,
      model,
      targetCustomers: chooseTarget(description),
      valueProposition: chooseValueProposition(description),
      revenueStreams: estimateRevenue(description),
      startupBudget: estimateBudget(description),
      cashflow: estimateCashflow(description),
      licenseRequirements: estimateLicenses(description),
      requiredSkills: estimateSkills(description),
      firstMillionTimeline: timelineFirstMillion(description),
      milestones: [
        'Month 1-3: Validate the idea, launch a minimum viable offer, and close the first paying customer.',
        'Month 4-6: Improve the offer, build repeatable sales, and secure a reliable marketing channel.',
        'Month 7-12: Create systems for delivery, scale revenue, and prepare for the next growth phase.',
      ],
      risks: [
        'Slow customer acquisition if marketing or positioning is unclear.',
        'Cashflow pressure during the first 3-6 months if revenues lag expectations.',
        'Competition from other small businesses and online alternatives.',
      ],
    };
    return plan;
  };

  const formatPlan = plan => {
    const budget = Object.entries(plan.startupBudget).map(([name, amount]) => `- ${name}: ${amount}`).join('\n');
    const cashflow = Object.entries(plan.cashflow).map(([period, detail]) => `- ${period}: ${detail}`).join('\n');
    const licenseList = plan.licenseRequirements.map(item => `- ${item}`).join('\n');
    const skills = plan.requiredSkills.map(item => `- ${item}`).join('\n');
    const milestones = plan.milestones.map(item => `- ${item}`).join('\n');
    const risks = plan.risks.map(item => `- ${item}`).join('\n');

    return `HOME BUSINESS PLAN\n===================\n\nBusiness description: ${plan.description}\nBusiness model: ${plan.model}\nTarget customers: ${plan.targetCustomers}\n\nValue proposition:\n${plan.valueProposition}\n\nRevenue streams:\n${plan.revenueStreams.map(item => `- ${item}`).join('\n')}\n\nStartup budget estimates:\n${budget}\n\nCashflow plan:\n${cashflow}\n\nLicense and compliance:\n${licenseList}\n\nRequired skills:\n${skills}\n\nFirst million timeline: ${plan.firstMillionTimeline}\n\nMilestones:\n${milestones}\n\nKey risks:\n${risks}\n`;
  };

  return {
    createPlan: buildPlan,
    formatPlan,
  };
})();

if (window.document) {
  const form = document.getElementById('plan-form');
  const ideaInput = document.getElementById('idea');
  const resultCard = document.getElementById('result-card');
  const resultArea = document.getElementById('result');
  const copyButton = document.getElementById('copy-button');

  if (form) {
    form.addEventListener('submit', event => {
      event.preventDefault();
      const idea = ideaInput.value.trim();
      if (!idea) return;
      const plan = BusinessPlanTool.createPlan(idea);
      resultArea.innerText = BusinessPlanTool.formatPlan(plan);
      resultCard.classList.remove('hidden');
    });
  }

  if (copyButton) {
    copyButton.addEventListener('click', async () => {
      const text = resultArea.innerText;
      try {
        await navigator.clipboard.writeText(text);
        copyButton.innerText = 'Copied!';
        setTimeout(() => (copyButton.innerText = 'Copy to clipboard'), 2000);
      } catch (error) {
        console.error(error);
      }
    });
  }
}
