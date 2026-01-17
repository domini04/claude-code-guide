# MCP Integration: Connecting External Tools

## What is MCP?

**MCP (Model Context Protocol)** is a standard protocol that allows Claude Code to connect with external tools and services. It extends Claude's capabilities beyond the local filesystem.

Think of MCP as a universal adapter that connects Claude to your entire development ecosystem.

## Boris's MCP Setup

Boris's team integrates multiple external tools via MCP:
- **Slack**: Read messages, post updates
- **BigQuery**: Run queries, analyze data
- **Sentry**: Read error logs, investigate issues

**Configuration**: `.mcp.json` in project root, shared across team

**On-demand loading**: Tools connect only when needed to prevent context bloat.

## Why MCP Matters

### Without MCP
```
User: What errors are users seeing?
Claude: I can't access Sentry. You'll need to check manually.
User: [Goes to Sentry, copies errors, pastes back]
```

### With MCP
```
User: What errors are users seeing?
Claude: [Connects to Sentry via MCP]
Claude: Found 3 errors in the last hour:
        1. TypeError in checkout.ts (23 occurrences)
        2. Network timeout in API calls (8 occurrences)
        3. Null reference in user profile (2 occurrences)
```

**Result**: Claude has real-time access to production data.

## Common MCP Use Cases

### 1. Communication (Slack, Discord)
- Read channel messages
- Post updates
- Search conversations
- Get notifications

### 2. Monitoring (Sentry, Datadog)
- Read error logs
- Analyze stack traces
- Track error trends
- Investigate incidents

### 3. Databases (PostgreSQL, BigQuery)
- Run read-only queries
- Analyze data
- Generate reports
- Validate migrations

### 4. Version Control (GitHub, GitLab)
- Read PR comments
- Check CI status
- Search issues
- Update labels

### 5. Project Management (Linear, Jira)
- Read issue descriptions
- Update issue status
- Search tickets
- Link code to issues

### 6. Documentation (Notion, Confluence)
- Search docs
- Read architecture decisions
- Update documentation
- Link to references

## Setting Up MCP

### 1. Install MCP Server

Each service requires an MCP server. Example for Slack:

```bash
npm install @anthropic/mcp-server-slack
```

### 2. Configure `.mcp.json`

Create `.mcp.json` in project root:

```json
{
  "mcpServers": {
    "slack": {
      "command": "node",
      "args": ["./node_modules/@anthropic/mcp-server-slack/dist/index.js"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}"
      }
    }
  }
}
```

### 3. Set Environment Variables

Create `.env`:
```
SLACK_BOT_TOKEN=xoxb-your-token-here
```

Add to `.gitignore`:
```
.env
.mcp.json.local
```

### 4. Use in Claude Code

```
User: What's the latest message in #engineering?
Claude: [Connects to Slack via MCP]
Claude: Latest message from Alice: "Deployed v2.3.0 to production"
```

## MCP Server Examples

### Slack Integration

**`.mcp.json`**:
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}"
      }
    }
  }
}
```

**Usage**:
```
User: Search Slack for discussions about authentication
Claude: [Searches Slack via MCP]
Claude: Found 5 threads discussing authentication...
```

### Sentry Integration

**`.mcp.json`**:
```json
{
  "mcpServers": {
    "sentry": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-sentry"],
      "env": {
        "SENTRY_AUTH_TOKEN": "${SENTRY_AUTH_TOKEN}",
        "SENTRY_ORG": "your-org",
        "SENTRY_PROJECT": "your-project"
      }
    }
  }
}
```

**Usage**:
```
User: What's causing the spike in errors today?
Claude: [Queries Sentry via MCP]
Claude: Error spike caused by: TypeError in payment processing
        Affecting 45 users in the last 2 hours
        Stack trace shows issue in checkout.ts:156
```

### BigQuery Integration

**`.mcp.json`**:
```json
{
  "mcpServers": {
    "bigquery": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-bigquery"],
      "env": {
        "GOOGLE_APPLICATION_CREDENTIALS": "${GOOGLE_APPLICATION_CREDENTIALS}",
        "PROJECT_ID": "your-project-id"
      }
    }
  }
}
```

**Usage**:
```
User: How many users signed up this week?
Claude: [Queries BigQuery via MCP]
Claude: Query results: 1,247 new users this week
        Up 23% from last week
```

### GitHub Integration

**`.mcp.json`**:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}",
        "GITHUB_REPO": "owner/repo"
      }
    }
  }
}
```

**Usage**:
```
User: What did reviewers say about my PR?
Claude: [Reads PR comments via GitHub MCP]
Claude: 3 comments from review:
        1. Sarah: "LGTM, just one question about error handling"
        2. Mike: "Can we add tests for the edge case?"
        3. Sarah: "Approved after discussion"
```

## On-Demand Loading

Boris's pattern: Load MCP servers only when needed.

**Benefits**:
- Prevents context bloat
- Faster startup
- Reduced memory usage

**Implementation**: MCP servers connect when first used, not at startup.

## Security Best Practices

### 1. Use Environment Variables

**Never hardcode credentials**:
```json
❌ "SLACK_BOT_TOKEN": "xoxb-actual-token-here"
✅ "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}"
```

### 2. Read-Only Access When Possible

For databases:
```json
{
  "mcpServers": {
    "postgres": {
      "env": {
        "DATABASE_USER": "readonly_user",
        "DATABASE_ROLE": "read_only"
      }
    }
  }
}
```

### 3. Scope Permissions Narrowly

For Slack:
- ✅ Read messages
- ❌ Delete messages
- ❌ Invite users

For GitHub:
- ✅ Read PRs
- ✅ Read issues
- ❌ Merge PRs
- ❌ Delete repos

### 4. Separate Production and Development

**Development** (`.mcp.json`):
```json
{
  "mcpServers": {
    "database": {
      "env": {
        "DATABASE_URL": "${DEV_DATABASE_URL}"
      }
    }
  }
}
```

**Production** (`.mcp.production.json`):
```json
{
  "mcpServers": {
    "database": {
      "env": {
        "DATABASE_URL": "${PROD_DATABASE_URL}",
        "DATABASE_READ_ONLY": "true"
      }
    }
  }
}
```

### 5. Audit MCP Access

Log MCP queries:
```json
{
  "mcpServers": {
    "postgres": {
      "env": {
        "LOG_QUERIES": "true",
        "LOG_FILE": "/var/log/mcp-postgres.log"
      }
    }
  }
}
```

## Team MCP Configuration

### Shared Configuration

Check `.mcp.json` into git (without secrets):
```json
{
  "mcpServers": {
    "slack": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}"
      }
    }
  }
}
```

### Personal Configuration

Create `.mcp.json.local` (gitignored):
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["@anthropic/mcp-server-notion"],
      "env": {
        "NOTION_TOKEN": "${MY_NOTION_TOKEN}"
      }
    }
  }
}
```

Add to `.gitignore`:
```
.mcp.json.local
.env
.env.local
```

## MCP Workflows

### Workflow 1: Error Investigation

```
User: Investigate the error spike in production
Claude: [Connects to Sentry via MCP]
Claude: Top error: TypeError in checkout.ts:156
Claude: [Reads the code]
Claude: Issue: Null check missing for user.paymentMethod
Claude: [Proposes fix]
User: Apply the fix and deploy
Claude: [Fixes code, runs tests, creates PR]
```

### Workflow 2: Data Analysis

```
User: Analyze user retention for this month
Claude: [Connects to BigQuery via MCP]
Claude: Query: SELECT ... FROM users WHERE ...
Claude: Results: 68% retention rate
Claude: Down 5% from last month
Claude: Main churn: Users who didn't complete onboarding
User: What can we improve in onboarding?
Claude: [Analyzes onboarding flow]
```

### Workflow 3: PR Review Integration

```
User: Update CLAUDE.md based on PR review comments
Claude: [Reads PR comments via GitHub MCP]
Claude: Found pattern in reviews:
        - Always validate user input
        - Use TypeScript strict mode
        - Add error boundaries for UI components
Claude: [Updates CLAUDE.md with these patterns]
```

### Workflow 4: Team Communication

```
User: Post a summary of today's changes to #engineering
Claude: [Summarizes git commits]
Claude: [Posts to Slack via MCP]
Claude: Posted to #engineering:
        "Today's updates:
        - Fixed authentication bug (#234)
        - Added dark mode toggle (#235)
        - Improved test coverage to 85%"
```

## Custom MCP Servers

You can create custom MCP servers for internal tools:

### Custom Server Structure

```typescript
// my-custom-mcp-server.ts
import { MCPServer } from '@anthropic/mcp-sdk';

const server = new MCPServer({
  name: 'custom-tool',
  version: '1.0.0',

  tools: {
    queryInternalAPI: async (params) => {
      // Your custom logic
      const result = await fetch('https://internal-api.com/data');
      return result.json();
    }
  }
});

server.start();
```

### Register Custom Server

```json
{
  "mcpServers": {
    "custom": {
      "command": "node",
      "args": ["./mcp-servers/my-custom-server.js"]
    }
  }
}
```

## MCP + CLAUDE.md Integration

Document MCP availability in CLAUDE.md:

```markdown
# External Tool Access

Available via MCP:
- Slack: Read/post messages in #engineering channel
- Sentry: Read error logs and stack traces
- BigQuery: Query analytics database (read-only)
- GitHub: Read PR comments and CI status

## When to Use MCP
- Investigating production errors: Use Sentry
- Analyzing user data: Use BigQuery
- Checking team discussions: Use Slack
- PR review integration: Use GitHub

## Important
- Database access is read-only
- Don't post to Slack without user confirmation
- Sentry access limited to last 30 days
```

## Troubleshooting MCP

### Problem: MCP server not connecting

**Check**:
1. Server installed: `npm list @anthropic/mcp-server-slack`
2. Environment variables set: `echo $SLACK_BOT_TOKEN`
3. Credentials valid: Test manually
4. Network access: Check firewall/VPN

### Problem: Authentication errors

**Solution**: Refresh credentials
```bash
# For OAuth tokens
npm run mcp:auth slack

# For API tokens
# Regenerate token in service dashboard
```

### Problem: MCP queries timing out

**Solution**: Add timeout configuration
```json
{
  "mcpServers": {
    "bigquery": {
      "timeout": 30000,  // 30 seconds
      "retries": 3
    }
  }
}
```

### Problem: Too many MCP requests

**Solution**: Implement rate limiting
```json
{
  "mcpServers": {
    "github": {
      "rateLimit": {
        "maxRequests": 100,
        "perMinutes": 60
      }
    }
  }
}
```

## MCP Best Practices

### 1. Start with Read-Only

Begin with read-only access:
- ✅ Query databases
- ✅ Read logs
- ✅ Search messages
- ❌ Write data (until you're comfortable)

### 2. Test in Development First

```bash
# Development MCP config
claude --mcp-config .mcp.dev.json

# Production MCP config
claude --mcp-config .mcp.prod.json
```

### 3. Document MCP Tools

In CLAUDE.md:
```markdown
# MCP Tools

## Sentry
- Tool: Read production errors
- Access: Read-only, last 30 days
- Usage: "What errors happened today?"

## BigQuery
- Tool: Query analytics
- Access: Read-only, analytics dataset only
- Usage: "How many users signed up this week?"
```

### 4. Monitor MCP Usage

Track what Claude queries:
```json
{
  "mcpServers": {
    "postgres": {
      "env": {
        "LOG_QUERIES": "true"
      }
    }
  }
}
```

Review logs:
```bash
tail -f /var/log/mcp-queries.log
```

## Next Steps

1. **Identify needs**: What external tools would help?
2. **Start simple**: Connect one tool (e.g., GitHub)
3. **Test thoroughly**: Verify read-only access works
4. **Document**: Add to CLAUDE.md
5. **Expand**: Add more tools as needed
6. **Share**: Team benefits from shared MCP configs

## Resources

- [MCP Documentation](https://modelcontextprotocol.org/)
- [Available MCP Servers](https://github.com/anthropics/mcp-servers)
- Boris's setup: [howborisusesclaudecode.com](https://howborisusesclaudecode.com/)
